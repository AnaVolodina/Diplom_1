# без неявного импорта не срабатывала команда запуска тестов pytest -v
import sys, os
print(f"test_ingredient.py __file__ = {__file__}")
print(f"test_ingredient.py sys.path BEFORE: {sys.path}")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог
print(f"test_ingredient.py sys.path AFTER: {sys.path}")

import pytest
from unittest.mock import Mock
from data import TestData


@pytest.fixture(autouse=True)
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_name.return_value = TestData.buns[0][0]
    bun_mock.get_price.return_value = TestData.buns[0][1]
    return bun_mock

@pytest.fixture(autouse=True)
def ingredient1_mock():
    ingredient_mock = Mock()
    ingredient_mock.get_name.return_value = TestData.ingredients[4][1]
    ingredient_mock.get_price.return_value = TestData.ingredients[4][2]
    ingredient_mock.get_type.return_value = TestData.INGREDIENT_TYPE_FILLING
    return ingredient_mock

@pytest.fixture(autouse=True)
def ingredient2_mock():
    ingredient2_mock = Mock()
    ingredient2_mock.get_name.return_value = TestData.ingredients[1][1]
    ingredient2_mock.get_price.return_value = TestData.ingredients[1][2]
    ingredient2_mock.get_type.return_value = TestData.INGREDIENT_TYPE_SAUCE
    return ingredient2_mock