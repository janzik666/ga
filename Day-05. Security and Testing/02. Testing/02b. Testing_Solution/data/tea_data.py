# data/tea_data.py
from models.tea import TeaModel
from models.comment import CommentModel
from models.user import UserModel

# ! We create some instances of our tea model here, which will be used in seeding.
teas_list = [
    TeaModel(name="chai", rating=4.3, in_stock=True, user_id=1),
    TeaModel(name="earl grey", rating=3, in_stock=False, user_id=2),
]

comments_list = [CommentModel(content="This is delicious", tea_id=1)]