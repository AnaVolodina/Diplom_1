import sys, os
print(f"test_ingredient.py __file__ = {__file__}")
print(f"test_ingredient.py sys.path BEFORE: {sys.path}")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог
print(f"test_ingredient.py sys.path AFTER: {sys.path}")
from database import Database
from data import TestData


class TestDatabase:
    def test_available_buns_get_name_success(self):
        database = Database()
        available_buns = database.available_buns()
        expected_bun_names = TestData.AVAILABLE_BUNS
        actual_bun_names = [bun.get_name() for bun in available_buns]
        assert expected_bun_names == actual_bun_names and len(database.available_buns()) == 3

    def test_available_ingredients_get_name_success(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        expected_ingredient_names = TestData.AVAILABLE_INGREDIENTS
        actual_ingredient_names = [ingredient.get_name() for ingredient in available_ingredients]
        assert expected_ingredient_names == actual_ingredient_names and len(database.available_ingredients()) == 6