import pytest
from data.classes import Category
from data.classes import Product
from data.classes import Smartphone
from data.classes import LawnGrass


@pytest.fixture
def smartphone_samsung():
    return Smartphone("Samsung Galaxy C23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0, 5, 500,
                      "Samsung Galaxy", "256GB", "Серый")


@pytest.fixture
def smartphone_samsung1():
    return Smartphone("Samsung Galaxy",
                      "256GB, Белый цвет",
                      100000.0, 10, 400,
                      "Samsung Galaxy", "256GB", "Белый")


@pytest.fixture
def smartphone(smartphone_samsung):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
                    [smartphone_samsung])


@pytest.fixture
def smartphone1(smartphone_samsung, smartphone_samsung1):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
                    [smartphone_samsung, smartphone_samsung1])


@pytest.fixture
def category_tv():
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
                    [])


@pytest.fixture
def tv_55QLED():
    return Product("55\" QLED 4K", "Фоновая подсветка",
                   123000.0, 7)


@pytest.fixture
def lw_dreams():
    return LawnGrass("Мечта садовника", "Неприхотлива",
                     1230.0, 17, "Россия", 20, "зеленая")


@pytest.fixture
def lawn_grass(lw_dreams):
    return Category("Трава газонная",
                    "Очень полезный товар",
                    [lw_dreams])


@pytest.fixture
def smartphone_new_samsung_0():
    return ["NEW Samsung Galaxy C23 Ultra", "NEW 256GB, Серый цвет, 200MP камера", 15000.0, 0, 400,
            "Samsung Galaxy", "256GB", "Серый"]


@pytest.fixture
def smartphone_new_samsung():
    return ["NEW Samsung Galaxy C23 Ultra", "NEW 256GB, Серый цвет, 200MP камера", 200000.0, 6, 400,
            "Samsung Galaxy", "256GB", "Серый"]


@pytest.fixture
def tv_new():
    return ["NEW tv", "NEW TV, Серый цвет", 220000.0, 16]


@pytest.fixture
def lw_new():
    return ["NEW lv", "NEW LV", 2100.0, 11, "Россия", 30, "Серый"]


def test_init_product(tv_55QLED):
    assert tv_55QLED.product_name == "55\" QLED 4K"
    assert tv_55QLED.product_description == "Фоновая подсветка"
    assert tv_55QLED.product_price == 123000.0
    assert tv_55QLED.product_quantity == 7


def test_init_category(smartphone, smartphone_samsung,
                       smartphone1, smartphone_samsung1,
                       category_tv):
    assert smartphone.category_name == "Смартфоны"
    assert smartphone.category_description == ("Смартфоны, как средство не только коммуникации, "
                                               "но и получение дополнительных функций для удобства жизни")
    assert smartphone.product_list == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
    assert smartphone1.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                        'Samsung Galaxy, 100000.0 руб. Остаток: 10 шт.\n')
    assert smartphone.category_total == 3
    assert smartphone.product_total == 3
    assert smartphone1.category_total == 3
    assert smartphone1.product_total == 3
    assert category_tv.category_total == 3
    assert category_tv.product_total == 3


def test_category_add_product_in_list(smartphone, smartphone_new_samsung,
                                      smartphone_new_samsung_0, category_tv, tv_new, lawn_grass, lw_new):
    new_prod = Smartphone.add_product(*smartphone_new_samsung)
    smartphone.add_product_in_list(new_prod)
    assert smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 200000.0 руб. Остаток: 6 шт.\n')

    new_prod = Smartphone.add_product(*smartphone_new_samsung_0)
    smartphone.add_product_in_list(new_prod)
    assert smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 200000.0 руб. Остаток: 6 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.\n')

    new_prod = LawnGrass.add_product(*lw_new)
    lawn_grass.add_product_in_list(new_prod)
    assert lawn_grass.product_list == ('Мечта садовника, 1230.0 руб. Остаток: 17 шт.\n'
                                       'NEW lv, 2100.0 руб. Остаток: 11 шт.\n')

    new_prod = Product.add_product(*tv_new)
    category_tv.add_product_in_list(new_prod)
    assert category_tv.product_list == 'NEW tv, 220000.0 руб. Остаток: 16 шт.\n'

    new_prod = Smartphone.add_product(*smartphone_new_samsung)
    assert lawn_grass.add_product_in_list(new_prod) == ("TypeError: adding <class 'data.classes.Smartphone'> into "
                                                        "Трава газонная\n Трава газонная is not Смартфоны")

    new_prod = LawnGrass.add_product(*lw_new)
    assert category_tv.add_product_in_list(new_prod) == ("TypeError: adding <class 'data.classes.LawnGrass'> "
                                                         "into Телевизоры\nТелевизоры is not Трава газонная")
    new_prod = Product.add_product(*tv_new)
    assert smartphone.add_product_in_list(new_prod) == ("TypeError: adding <class 'data.classes.Product'> "
                                                        "into Смартфоны\nСмартфоны is not Product")

    new_prod = []
    assert smartphone.add_product_in_list(new_prod) == "TypeError: <class 'list'> is not Product"


def test_new_price(smartphone, smartphone_new_samsung_0):
    new_prod = Smartphone.add_product(*smartphone_new_samsung_0)
    new_prod.product_price = 0
    smartphone.add_product_in_list(new_prod)
    assert smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.\n')
    new_prod = Smartphone.add_product(*smartphone_new_samsung_0)
    new_prod.product_price = 20
    smartphone.add_product_in_list(new_prod)
    assert smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 20.0 руб. Остаток: 0 шт.\n')

    new_prod = Smartphone.add_product(*smartphone_new_samsung_0)
    new_prod.product_price = -20
    smartphone.add_product_in_list(new_prod)
    assert smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 20.0 руб. Остаток: 0 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 15000.0 руб. Остаток: 0 шт.\n')


def test_str_category(smartphone1):
    assert str(smartphone1) == ('Смартфоны, количество продуктов: 15 шт.\n'
                                'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                'Samsung Galaxy, 100000.0 руб. Остаток: 10 шт.\n')


def test_str_product(smartphone_samsung):
    assert str(smartphone_samsung) == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'


def test_repr_category(smartphone):
    assert repr(smartphone) == ("Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, "
                                "но и получение дополнительных функций для удобства жизни', "
                                "[Smartphone('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', "
                                "180000.0, 5, 500, 'Samsung Galaxy', '256GB', 'Серый')])\n"
                                "Category.category_total: 9, Category.product_total: 9")


def test_repr_smartphone(smartphone_samsung):
    assert repr(smartphone_samsung) == ("Smartphone('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP "
                                        "камера', 180000.0, 5, 500, 'Samsung Galaxy', '256GB', 'Серый')")


def test_repr_lawn_grass(lw_dreams):
    assert repr(lw_dreams) == "LawnGrass('Мечта садовника', 'Неприхотлива',1230.0, 17,'Россия', '20', зеленая)"


def test_repr_product(tv_55QLED):
    assert repr(tv_55QLED) == "Product('55\" QLED 4K', 'Фоновая подсветка', 123000.0, 7)"


def test_len_category(smartphone1, lawn_grass, category_tv):
    assert len(smartphone1) == 15
    assert len(lawn_grass) == 17
    assert len(category_tv) == 0


def test_len_product(smartphone_samsung1, tv_55QLED, lw_dreams):
    assert len(smartphone_samsung1) == 10
    assert len(tv_55QLED) == 7
    assert len(lw_dreams) == 17


def test_add_product(smartphone_samsung, smartphone_samsung1, tv_55QLED, lw_dreams):
    assert smartphone_samsung + smartphone_samsung1 == 100000 * 10 + 180000 * 5
    assert smartphone_samsung + tv_55QLED == 'TypeError: different classes'
    assert lw_dreams + tv_55QLED == 'TypeError: different classes'
