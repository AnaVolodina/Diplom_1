import sys, os
print(f"test_ingredient.py __file__ = {__file__}")
print(f"test_ingredient.py sys.path BEFORE: {sys.path}")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог
print(f"test_ingredient.py sys.path AFTER: {sys.path}")
import pytest
from bun import Bun
from data import TestData


class TestBun:
    @pytest.mark.parametrize('name, price, expected_name',
                             ((TestData.buns[0][0], TestData.buns[0][1], TestData.FIRST_BUN_NAME),
                              (TestData.buns[1][0], TestData.buns[1][1], TestData.SECOND_BUN_NAME),
                              (TestData.buns[2][0], TestData.buns[2][1], TestData.THIRD_BUN_NAME))
                             )
    def test_get_name_success(self, name, price, expected_name):
        bun = Bun(name, price)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize('name, price, expected_price',
                             ((TestData.buns[0][0], TestData.buns[0][1], TestData.FIRST_BUN_PRICE),
                              (TestData.buns[1][0], TestData.buns[1][1], TestData.SECOND_BUN_PRICE),
                              (TestData.buns[2][0], TestData.buns[2][1], TestData.THIRD_BUN_PRICE))
                             )
    def test_get_price_success(self, name, price, expected_price):
        bun = Bun(name, price)
        assert bun.get_price() == expected_price