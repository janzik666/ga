from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from models.user import UserModel
from database import get_db
import jwt
from jwt import DecodeError, ExpiredSignatureError # We import specific exceptions to handle them explicitly
from config.environment import secret

# We're using HTTP Bearer scheme for Authorization header
http_bearer = HTTPBearer()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(http_bearer)):
    # This function is a dependency that takes in the database session and the JWT token from the request header

    try:
        # We try to decode the token using the secret key
        payload = jwt.decode(token.credentials, secret, algorithms=["HS256"])

        # We then query the database to find the user with the id specified in the token's payload
        user = db.query(UserModel).filter(UserModel.id == payload.get("sub")).first()

        # If the user doesn't exist, we raise an HTTP 401 Unauthorized error
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid username or password")

    # If there is a DecodeError while decoding the token, we raise an HTTP 403 Forbidden error
    except DecodeError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail=f'Could not decode token: {str(e)}')

    # If the token has expired, we also raise an HTTP 403 Forbidden error
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Token has expired')

    # If everything is successful, we return the user
    return user
