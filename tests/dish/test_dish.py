from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish("lasanha de carne com camarão", 30.00)
    assert dish.name == "lasanha de carne com camarão"
    assert dish.price == 30.00
    assert dish.recipe == {}

    assert dish.__repr__() == f"Dish('{dish.name}', R${dish.price:.2f})"
    assert dish.__eq__(dish) is True
    assert dish.__hash__() == hash(dish.__repr__())

    dish.add_ingredient_dependency(Ingredient("massa de lasanha"), 200)
    dish.add_ingredient_dependency(Ingredient("presunto"), 200)
    dish.add_ingredient_dependency(Ingredient("queijo mussarela"), 300)
    dish.add_ingredient_dependency(Ingredient("camarão"), 200)
    dish.add_ingredient_dependency(Ingredient("carne"), 500)
    assert dish.recipe == {
        Ingredient("massa de lasanha"): 200,
        Ingredient("presunto"):  200,
        Ingredient("queijo mussarela"): 300,
        Ingredient("camarão"): 200,
        Ingredient("carne"): 500
    }

    assert dish.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
        Restriction.SEAFOOD,
    }

    assert  dish.get_ingredients() == {
        Ingredient("massa de lasanha"),
        Ingredient("presunto"),
        Ingredient("queijo mussarela"),
        Ingredient("camarão"),
        Ingredient("carne")
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("lasanha de carne com camarão", "30")

    with pytest.raises(ValueError, match="Dish price must be greater then zero."):
        Dish("lasanha de carne com camarão", -30)

