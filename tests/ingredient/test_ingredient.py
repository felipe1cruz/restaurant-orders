from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("bacon")
    assert ingredient.name == "bacon"
    # testa atributo restrictions
    assert ingredient.restrictions == {"ANIMAL_MEAT", "ANIMAL_DERIVED"}
    # testa método mágico __repr__
    assert repr(ingredient) == "Ingredient('bacon')"
    # testa método mágico __eq__
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("cheese")
    assert ingredient == ingredient2
    assert ingredient != ingredient3
    # testa método mágico __hash__
    assert hash(ingredient) == hash(ingredient2)
