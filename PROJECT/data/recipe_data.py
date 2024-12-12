from models.recipe import RecipeModel
from models.ingredient import IngredientModel
from models.step import StepModel

recipes_list = [
    RecipeModel(title="Veal Piccata", recipe_type="entree", cuisine_tags="Italian, veal, pasta", serves=4, notes="", user_id=1),
    RecipeModel(title="Baked Mac and Cheese", recipe_type="entree", cuisine_tags="pasta", serves=8, notes="",user_id=1)    
]

ingredients_list = [
    IngredientModel(name="Angel Hair Pasta", quantity="1lb", recipe_id=1),
    IngredientModel(name="All purpose flour", quantity="1/2 cup", recipe_id=1),
    IngredientModel(name="Salt", quantity="To taste", recipe_id=1),
    IngredientModel(name="Pepper", quantity="To taste", recipe_id=1),
    IngredientModel(name="Veal cutlet", quantity="1lb", recipe_id=1),
    IngredientModel(name="Chicken stock", quantity="1 cup", recipe_id=1),
    IngredientModel(name="White wine or cooking sherry", quantity="1/2 cup", recipe_id=1),
    IngredientModel(name="Lemon juice", quantity="1 lemon", recipe_id=1),
    IngredientModel(name="Capers", quantity="To taste", recipe_id=1),
    IngredientModel(name="Salted butter", quantity="4 tablespoons", recipe_id=1),
    IngredientModel(name="Chopped parsley", quantity="2 tablespoons", recipe_id=1),
    ]
steps_list = [
    StepModel(step_order=1, step_details='Preheat oven to 350F', recipe_id=1),
    StepModel(step_order=2, step_details='Cook pasta to al dente', recipe_id=1),
    StepModel(step_order=3, step_details='Combine flour, salt, pepper in shallow bowl', recipe_id=1),
    StepModel(step_order=4, step_details='Heat up large pan, add 2 tablespoon oil, heat for another 30 seconds.', recipe_id=1),
    StepModel(step_order=5, step_details='Dredge veal cutlet in flour mixture and move to clean plate.', recipe_id=1),
    StepModel(step_order=6, step_details='Add to hot pan for 2-3 minutes each side, work in batches. Set aside on covered plate to keep warm.', recipe_id=1),
    StepModel(step_order=7, step_details='In between veal frying, combine stock, wine, lemon juice and capers.  After all cutlets have been cooked deglaze pan.', recipe_id=1),
    StepModel(step_order=8, step_details='Bring liquid to a boil, then lower to a simmer and cook for about 3 minutes or until mixture reduces in half.', recipe_id=1),
    StepModel(step_order=9, step_details='Swirl in butter until melted.  Add Parsley', recipe_id=1),
    StepModel(step_order=10, step_details='Stir in pasta with mixture in pan.  Top with veal cutlets.', recipe_id=1)
    ]
    