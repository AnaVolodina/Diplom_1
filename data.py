class TestData:
    buns = [['black bun', 100],
            ['white bun', 200],
            ['red bun', 300]]


    ingredients = [
        ['Соусы', 'hot sauce', 100],
        ['Соусы', 'sour cream', 200],
        ['Соусы', 'chili sauce', 300],
        ['Начинки', 'cutlet', 100],
        ['Начинки', 'dinosaur', 200],
        ['Начинки', 'sausage', 300]
    ]

    FIRST_BUN_NAME = 'black bun'
    SECOND_BUN_NAME = 'white bun'
    THIRD_BUN_NAME = 'red bun'
    FIRST_BUN_PRICE = 100
    SECOND_BUN_PRICE = 200
    THIRD_BUN_PRICE = 300
    RECEIPT = ('(==== black bun ====)\n= filling dinosaur =\n= sauce sour cream =\n(==== black bun ====)\n\nPrice: 600')
    AVAILABLE_BUNS = ['black bun', 'white bun', 'red bun']
    AVAILABLE_INGREDIENTS = ['hot sauce', 'sour cream', 'chili sauce', 'cutlet', 'dinosaur', 'sausage']
    INGREDIENT_TYPE_SAUCE = 'SAUCE'
    INGREDIENT_TYPE_FILLING = 'FILLING'