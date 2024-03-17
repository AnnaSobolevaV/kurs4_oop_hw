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
def category_TV():
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
                    [])

def test_init_product(category_smartphone_samsung):
    assert category_smartphone_samsung.product_name == "Samsung Galaxy C23 Ultra"
    assert category_smartphone_samsung.product_description == "256GB, Серый цвет, 200MP камера"
    assert category_smartphone_samsung.product_price == 180000.0
    assert category_smartphone_samsung.product_quantity == 5


def test_init_category(category_smartphone, category_smartphone_samsung,
                       category_smartphone1, category_smartphone_samsung1,
                       category_TV):
    assert category_smartphone.category_name == "Смартфоны"
    assert category_smartphone.category_description == ("Смартфоны, как средство не только коммуникации, "
                                                        "но и получение дополнительных функций для удобства жизни")
    assert category_smartphone.product_list == [category_smartphone_samsung]
    assert category_smartphone1.product_list == [category_smartphone_samsung, category_smartphone_samsung1]
    assert category_smartphone.category_total == 3
    assert category_smartphone.product_total == 3
    assert category_smartphone1.category_total == 3
    assert category_smartphone1.product_total == 3
    assert category_TV.category_total == 3
    assert category_TV.product_total == 3
