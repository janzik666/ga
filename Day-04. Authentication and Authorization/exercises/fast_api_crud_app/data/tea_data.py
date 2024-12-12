# data/tea_data.py
from models.tea import TeaModel
from models.comment import CommentModel

teas_list = [
    TeaModel(name="chai", rating=4, in_stock=True),
    TeaModel(name="earl grey", rating=3, in_stock=False)
]

# ! Specify the tea_id on the CommentModel, to associate it with a tea
comments_list = [CommentModel(content="This is a great tea", tea_id=1)]