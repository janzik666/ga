from models.tea import TeaModel
from models.comment import CommentModel
from models.user import UserModel # Import user model

teas_list = [
  TeaModel(name="chai", rating=4, in_stock=True, user_id=1),
  TeaModel(name="earl grey", rating=3, in_stock=False, user_id=2)
]

# ! Specify the tea_id on the CommentModel, to associate it with a tea
comments_list = [CommentModel(content="This is a great tea", tea_id=1)]