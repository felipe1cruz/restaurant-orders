import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish = Dish("macarrao", 20.99)
    assert dish.name == "macarrao"
    assert dish.price == 20.99
    assert dish.recipe == {}

    expected_repr = "Dish('macarrao', R$20.99)"
    assert repr(dish) == expected_repr

    dish2 = Dish("macarrao", 20.99)
    dish3 = Dish("feijao", 14.99)
    assert dish == dish2
    assert dish != dish3

    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish3)

    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("eggs")
    dish.add_ingredient_dependency(ingredient1, 100)
    dish.add_ingredient_dependency(ingredient2, 50)
    assert dish.recipe.get(ingredient1) == 100
    assert dish.recipe.get(ingredient2) == 50

    expected_restrictions = {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert dish.get_restrictions() == expected_restrictions

    expected_ingredients = {ingredient1, ingredient2}

    assert dish.get_ingredients() == expected_ingredients

    with pytest.raises(TypeError):
        Dish("macarrao", "20.99")

    with pytest.raises(ValueError):
        Dish("macarrao", -2)
