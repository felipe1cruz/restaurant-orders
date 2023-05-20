import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path):
        with open(source_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                dish_name, price, ingredient_name, ingredient_quantity = row
                price = float(price)
                ingredient_quantity = int(ingredient_quantity)

                dish = self.find_dish(dish_name)
                if dish is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, ingredient_quantity)

    def find_dish(self, dish_name):
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish
        return None
