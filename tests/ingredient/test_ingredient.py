from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("camarão")
    assert ingredient.name == "camarão"
    assert ingredient.restrictions == {
            Restriction.ANIMAL_MEAT,
            Restriction.SEAFOOD,
            Restriction.ANIMAL_DERIVED,
        }
    assert ingredient.__repr__()  == "Ingredient('camarão')"
    assert ingredient.__eq__(ingredient) is True
    assert ingredient.__hash__() == hash(ingredient.name)


