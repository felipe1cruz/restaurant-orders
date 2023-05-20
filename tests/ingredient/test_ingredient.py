from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("bacon")
    assert ingredient.name == "bacon"
    # testa atributo restrictions
    expected_restrictions = {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert ingredient.restrictions == expected_restrictions
    # testa método mágico __repr__
    assert repr(ingredient) == "Ingredient('bacon')"
    # testa método mágico __eq__
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("cheese")
    assert ingredient == ingredient2
    assert ingredient != ingredient3
    # testa método mágico __hash__
    assert hash(ingredient) == hash(ingredient2)
    assert hash(ingredient) != hash(ingredient3)
