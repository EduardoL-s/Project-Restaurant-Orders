import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, 'r') as arquivo:
            arquivo_csv =  list(csv.DictReader(arquivo))
            dish_exist = {}

            for row in arquivo_csv:
                dish = dish_exist.setdefault(
                    row['dish'],
                    Dish(row['dish'], float(row['price'])))

                dish.add_ingredient_dependency(
                    Ingredient(row['ingredient']),
                    int(row['recipe_amount']))
                self.dishes.add(dish)

            
