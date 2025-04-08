Дипломный проект. Задание 1: Юнит-тесты
Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers
Реализованные сценарии
Созданы юнит-тесты, покрывающие классы Bun, Burger, Ingredient, Database

Процент покрытия 100% (отчет: htmlcov/index.html)

Структура проекта
код программы содержится в файлах bun.py, burger.py, database.py, ingredient.py, ingredient_types.py, praktikum.py.
tests - пакет, содержащий тесты, разделённые по классам. Например, bun_test.py, burger_test.py и т.д.
conftest.py- файл с фикстурами.
data.py - файл со вспомогательными данными.
Запуск автотестов
Установка зависимостей

$ pip install -r requirements.txt

Запуск автотестов и создание HTML-отчета о покрытии

$ pytest --cov=Diplom_1 --cov-report=html