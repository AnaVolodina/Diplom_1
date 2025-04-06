import sys, os
print(f"test_ingredient.py __file__ = {__file__}")
print(f"test_ingredient.py sys.path BEFORE: {sys.path}")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог
print(f"test_ingredient.py sys.path AFTER: {sys.path}")
from burger import Burger
from data import TestData


class TestBurger:
    def test_set_buns_success(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient_success(self, ingredient1_mock):
        burger = Burger()
        burger.add_ingredient(ingredient1_mock)
        assert burger.ingredients == [ingredient1_mock]

    def test_remove_ingredient_success(self, ingredient1_mock, ingredient2_mock):
        burger = Burger()
        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1 and ingredient2_mock in burger.ingredients

    def test_move_ingredient_success(self, ingredient1_mock, ingredient2_mock):
        burger = Burger()
        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient1_mock and burger.ingredients[0] == ingredient2_mock

    def test_get_price_success(self, bun_mock, ingredient2_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient2_mock)
        expected_price = bun_mock.get_price() * 2 + ingredient2_mock.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_success(self, bun_mock, ingredient1_mock, ingredient2_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.bun = bun_mock
        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)
        burger.ingredients = [ingredient1_mock, ingredient2_mock]
        expected_receipt = TestData.RECEIPT
        assert burger.get_receipt() == expected_receipt
