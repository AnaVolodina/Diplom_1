import sys, os
print(f"test_ingredient.py __file__ = {__file__}")
print(f"test_ingredient.py sys.path BEFORE: {sys.path}")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог
print(f"test_ingredient.py sys.path AFTER: {sys.path}")
import pytest
from ingredient import Ingredient
from data import TestData


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_get_price_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_get_name_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_get_type_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
