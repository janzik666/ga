# controllers/comments.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.comment import CommentModel
from serializers.comment import CommentSchema
from typing import List
from database import get_db

router = APIRouter()


@router.get("/comments", response_model=List[CommentSchema])
def get_comments(db: Session = Depends(get_db)):
    comments = db.query(CommentModel).all()
    return comments

@router.get("/comments/{comment_id}", response_model=CommentSchema)
def get_single_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not comment:
         raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.post("/comments", response_model=CommentSchema)
def create_comment(comment: CommentSchema, db: Session = Depends(get_db)):
    new_comment = CommentModel(**comment.dict())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.put("/comments/{comment_id}", response_model=CommentSchema)
def update_comment(comment_id: int, comment: CommentSchema, db: Session = Depends(get_db)):
    db_comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    
    #update the comments
    comment_data = comment.dict(exclude_unset=True)
    for key, value in comment_data.items():
        setattr(db_comment, key, value)
    
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    #find the comment to delete
    db_comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    db.delete(db_comment)
    db.commit()
    return {"message": f"Comment {comment_id} deleted successfully"}

    
