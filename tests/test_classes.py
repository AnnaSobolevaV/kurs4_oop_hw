import pytest
from data.classes import Category
from data.classes import Product


@pytest.fixture
def category_smartphone_samsung():
    return Product("Samsung Galaxy C23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


@pytest.fixture
def category_smartphone_samsung1():
    return Product("Samsung Galaxy",
                   "256GB, Белый цвет",
                   100000.0, 10)


@pytest.fixture
def category_smartphone(category_smartphone_samsung):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
                    [category_smartphone_samsung])


@pytest.fixture
def category_smartphone1(category_smartphone_samsung, category_smartphone_samsung1):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
                    [category_smartphone_samsung, category_smartphone_samsung1])


@pytest.fixture
def category_tv():
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
                    [])


@pytest.fixture
def category_smartphone_new_samsung_0():
    return ["NEW Samsung Galaxy C23 Ultra", "NEW 256GB, Серый цвет, 200MP камера", 15000.0, 0]


@pytest.fixture
def category_smartphone_new_samsung():
    return ["NEW Samsung Galaxy C23 Ultra", "NEW 256GB, Серый цвет, 200MP камера", 200000.0, 6]


def test_init_product(category_smartphone_samsung):
    assert category_smartphone_samsung.product_name == "Samsung Galaxy C23 Ultra"
    assert category_smartphone_samsung.product_description == "256GB, Серый цвет, 200MP камера"
    assert category_smartphone_samsung.product_price == 180000.0
    assert category_smartphone_samsung.product_quantity == 5


def test_init_category(category_smartphone, category_smartphone_samsung,
                       category_smartphone1, category_smartphone_samsung1,
                       category_tv):
    assert category_smartphone.category_name == "Смартфоны"
    assert category_smartphone.category_description == ("Смартфоны, как средство не только коммуникации, "
                                                        "но и получение дополнительных функций для удобства жизни")
    assert category_smartphone.product_list == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert category_smartphone1.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                                 'Samsung Galaxy, 100000.0 руб. Остаток: 10 шт.')
    assert category_smartphone.category_total == 3
    assert category_smartphone.product_total == 3
    assert category_smartphone1.category_total == 3
    assert category_smartphone1.product_total == 3
    assert category_tv.category_total == 3
    assert category_tv.product_total == 3


def test_category_add_product_in_list(category_smartphone, category_smartphone_new_samsung,
                                      category_smartphone_new_samsung_0):
    new_prod = Product.add_product(*category_smartphone_new_samsung)
    category_smartphone.add_product_in_list(new_prod)
    assert category_smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                                'NEW Samsung Galaxy C23 Ultra, 200000.0 руб. Остаток: 6 шт.')

    new_prod = Product.add_product(*category_smartphone_new_samsung_0)
    category_smartphone.add_product_in_list(new_prod)
    assert category_smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                                'NEW Samsung Galaxy C23 Ultra, 200000.0 руб. Остаток: 6 шт.\n'
                                                'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.')


def test_new_price(category_smartphone, category_smartphone_new_samsung_0):
    new_prod = Product.add_product(*category_smartphone_new_samsung_0)
    new_prod.product_price = 0
    category_smartphone.add_product_in_list(new_prod)
    assert category_smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                                'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.')
    new_prod = Product.add_product(*category_smartphone_new_samsung_0)
    new_prod.product_price = 20
    category_smartphone.add_product_in_list(new_prod)
    assert category_smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                                'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.\n'
                                                'NEW Samsung Galaxy C23 Ultra, 20.0 руб. Остаток: 0 шт.')

    new_prod = Product.add_product(*category_smartphone_new_samsung_0)
    new_prod.product_price = -20
    category_smartphone.add_product_in_list(new_prod)
    assert category_smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                                'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.\n'
                                                'NEW Samsung Galaxy C23 Ultra, 20.0 руб. Остаток: 0 шт.\n'
                                                'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.')
