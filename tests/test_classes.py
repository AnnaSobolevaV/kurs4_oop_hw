import pytest
from data.classes import Category, Order
from data.classes import Product
from data.classes import Smartphone
from data.classes import LawnGrass


@pytest.fixture
def smartphone_samsung0():
    return Smartphone("Samsung Galaxy C23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0, 0, 500,
                      "Samsung Galaxy", "256GB", "Серый")


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
def tv_new_0():
    return ["NEW tv", "NEW TV, Серый цвет", 220000.0, 0]


@pytest.fixture
def lw_new():
    return ["NEW lv", "NEW LV", 2100.0, 11, "Россия", 30, "Серый"]


@pytest.fixture
def lw_new_0():
    return ["NEW lv", "NEW LV", 2100.0, 0, "Россия", 30, "Серый"]


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


def test_category_add_product_in_list(smartphone, smartphone_new_samsung, smartphone_samsung0, category_tv, tv_new,
                                      lawn_grass, lw_new):
    new_prod = Smartphone.add_product(*smartphone_new_samsung)
    smartphone.add_product_in_list(new_prod)
    assert smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 200000.0 руб. Остаток: 6 шт.\n')

    new_prod = LawnGrass.add_product(*lw_new)
    lawn_grass.add_product_in_list(new_prod)
    assert lawn_grass.product_list == ('Мечта садовника, 1230.0 руб. Остаток: 17 шт.\n'
                                       'NEW lv, 2100.0 руб. Остаток: 11 шт.\n')

    new_prod = Product.add_product(*tv_new)
    category_tv.add_product_in_list(new_prod)
    assert category_tv.product_list == 'NEW tv, 220000.0 руб. Остаток: 16 шт.\n'

    new_prod = Smartphone.add_product(*smartphone_new_samsung)
    assert lawn_grass.add_product_in_list(new_prod) == "<class 'data.classes.Smartphone'> is added to Трава газонная"

    new_prod = LawnGrass.add_product(*lw_new)
    assert category_tv.add_product_in_list(new_prod) == "<class 'data.classes.LawnGrass'> is added to Телевизоры"
    new_prod = Product.add_product(*tv_new)
    assert smartphone.add_product_in_list(new_prod) == "<class 'data.classes.Product'> is added to Смартфоны"

    new_prod = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with pytest.raises(TypeError, match="<class 'list'> is not Product"):
        smartphone.add_product_in_list(new_prod)

    assert smartphone.add_product_in_list(smartphone_samsung0) == "You can't add a product with 0 quantity"


def test_new_price(smartphone, smartphone_new_samsung):
    new_prod = Smartphone.add_product(*smartphone_new_samsung)
    new_prod.product_price = 0
    smartphone.add_product_in_list(new_prod)
    assert smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 200000.0 руб. Остаток: 6 шт.\n')
    new_prod = Smartphone.add_product(*smartphone_new_samsung)
    new_prod.product_price = 20
    smartphone.add_product_in_list(new_prod)
    assert smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 200000.0 руб. Остаток: 6 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 20.0 руб. Остаток: 6 шт.\n')

    new_prod = Smartphone.add_product(*smartphone_new_samsung)
    new_prod.product_price = -20
    smartphone.add_product_in_list(new_prod)
    assert smartphone.product_list == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 200000.0 руб. Остаток: 6 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 20.0 руб. Остаток: 6 шт.\n'
                                       'NEW Samsung Galaxy C23 Ultra, 200000.0 руб. Остаток: 6 шт.\n')


def test_str_category(smartphone1):
    assert str(smartphone1) == ('Смартфоны, количество продуктов: 15 шт.\n'
                                'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                'Samsung Galaxy, 100000.0 руб. Остаток: 10 шт.\n')


def test_str_product(smartphone_samsung):
    assert str(smartphone_samsung) == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'


def test_repr_category(smartphone):
    assert repr(smartphone) == ("<<class 'data.classes.Category'>, {'category_name': 'Смартфоны', "
                                "'category_description': 'Смартфоны, как средство не только коммуникации, "
                                "но и получение дополнительных функций для удобства жизни', "
                                "'_Category__product_list': [<<class 'data.classes.Smartphone'>, {'product_name': "
                                "'Samsung Galaxy C23 Ultra', 'product_description': '256GB, Серый цвет, "
                                "200MP камера', '_Product__product_price': 180000.0, 'product_quantity': 5, "
                                "'performance': 500, 'model': 'Samsung Galaxy', 'memory': '256GB', "
                                "'color': 'Серый'}>]}>")


def test_repr_smartphone(smartphone_samsung):
    assert repr(smartphone_samsung) == ("<<class 'data.classes.Smartphone'>, {'product_name': 'Samsung Galaxy C23 "
                                        "Ultra', 'product_description': '256GB, Серый цвет, 200MP камера', "
                                        "'_Product__product_price': 180000.0, 'product_quantity': 5, 'performance': "
                                        "500, 'model': 'Samsung Galaxy', 'memory': '256GB', 'color': 'Серый'}>")


def test_repr_lawn_grass(lw_dreams):
    assert repr(lw_dreams) == ("<<class 'data.classes.LawnGrass'>, {'product_name': 'Мечта садовника', "
                               "'product_description': 'Неприхотлива', '_Product__product_price': 1230.0, "
                               "'product_quantity': 17, 'country': 'Россия', 'germ_period': 20, 'color': 'зеленая'}>")


def test_repr_product(tv_55QLED):
    assert repr(tv_55QLED) == ("<<class 'data.classes.Product'>, {'product_name': '55\" QLED 4K', "
                               "'product_description': 'Фоновая подсветка', '_Product__product_price': 123000.0, "
                               "'product_quantity': 7}>")


def test_len_category(smartphone1, lawn_grass, category_tv):
    assert len(smartphone1) == 15
    assert len(lawn_grass) == 17
    assert len(category_tv) == 0


def test_len_product(smartphone_samsung1, tv_55QLED, lw_dreams):
    assert len(smartphone_samsung1) == 10
    assert len(tv_55QLED) == 7
    assert len(lw_dreams) == 17


def test_add_(smartphone_samsung, smartphone_samsung1, tv_55QLED, lw_dreams):
    assert smartphone_samsung + smartphone_samsung1 == 100000 * 10 + 180000 * 5
    with pytest.raises(TypeError, match="You can't add different classes"):
        smartphone_samsung + tv_55QLED
    with pytest.raises(TypeError, match="You can't add different classes"):
        lw_dreams + tv_55QLED
    with pytest.raises(TypeError, match="You can't add different classes"):
        tv_55QLED + lw_dreams


def test_obj_creation_log(smartphone, smartphone_new_samsung, category_tv, tv_new, lawn_grass, lw_new):
    new_prod = Smartphone.add_product(*smartphone_new_samsung)
    assert new_prod.obj_creation_log() == ("MixinLog: created: <<class 'data.classes.Smartphone'>, {'product_name': "
                                           "'NEW Samsung Galaxy C23 Ultra', 'product_description': 'NEW 256GB, "
                                           "Серый цвет, 200MP камера', '_Product__product_price': 200000.0, "
                                           "'product_quantity': 6, 'performance': 400, 'model': 'Samsung Galaxy', "
                                           "'memory': '256GB', 'color': 'Серый'}>")
    new_prod = LawnGrass.add_product(*lw_new)
    assert new_prod.obj_creation_log() == ("MixinLog: created: <<class 'data.classes.LawnGrass'>, {'product_name': "
                                           "'NEW lv', 'product_description': 'NEW LV', '_Product__product_price': "
                                           "2100.0, 'product_quantity': 11, 'country': 'Россия', 'germ_period': 30, "
                                           "'color': 'Серый'}>")

    new_prod = Product.add_product(*tv_new)
    assert new_prod.obj_creation_log() == ("MixinLog: created: <<class 'data.classes.Product'>, {'product_name': 'NEW "
                                           "tv', 'product_description': 'NEW TV, Серый цвет', "
                                           "'_Product__product_price': 220000.0, 'product_quantity': 16}>")

    assert category_tv.obj_creation_log() == ("MixinLog: created: <<class 'data.classes.Category'>, {'category_name': "
                                              "'Телевизоры', 'category_description': 'Современный телевизор, "
                                              "который позволяет наслаждаться просмотром, станет вашим другом и "
                                              "помощником', '_Category__product_list': []}>")
    assert lawn_grass.obj_creation_log() == ("MixinLog: created: <<class 'data.classes.Category'>, {'category_name': "
                                             "'Трава газонная', 'category_description': 'Очень полезный товар', "
                                             "'_Category__product_list': [<<class 'data.classes.LawnGrass'>, "
                                             "{'product_name': 'Мечта садовника', 'product_description': "
                                             "'Неприхотлива', '_Product__product_price': 1230.0, 'product_quantity': "
                                             "17, 'country': 'Россия', 'germ_period': 20, 'color': 'зеленая'}>]}>")
    assert smartphone.obj_creation_log() == ("MixinLog: created: <<class 'data.classes.Category'>, {'category_name': "
                                             "'Смартфоны', 'category_description': 'Смартфоны, как средство не только "
                                             "коммуникации, но и получение дополнительных функций для удобства "
                                             "жизни', '_Category__product_list': [<<class 'data.classes.Smartphone'>, "
                                             "{'product_name': 'Samsung Galaxy C23 Ultra', 'product_description': "
                                             "'256GB, Серый цвет, 200MP камера', '_Product__product_price': 180000.0, "
                                             "'product_quantity': 5, 'performance': 500, 'model': 'Samsung Galaxy', "
                                             "'memory': '256GB', 'color': 'Серый'}>]}>")


def test_init_order(smartphone_samsung):
    order = Order()
    assert order.order_id == 1
    assert order.order_number == 1
    assert order.product_list == ''
    assert order.product_total == 0
    assert order.cost == 0.0
    assert order.add_product_in_list(smartphone_samsung) == "<class 'data.classes.Smartphone'> is added to Order №1"
    assert order.order_id == 1
    with pytest.raises(TypeError, match="<class 'list'> is not Product"):
        order.add_product_in_list([1, 2])
    assert order.order_id == 1


def test_repr_order(smartphone_samsung):
    order = Order()
    assert repr(order) == ("<<class 'data.classes.Order'>, {'_Order__product_list': [],"
                           " 'order_number': 2, 'product_total': 0, 'cost': 0}>")
    order.add_product_in_list(smartphone_samsung)
    assert repr(order) == ("<<class 'data.classes.Order'>, {'_Order__product_list': [[<<class "
                           "'data.classes.Smartphone'>, {'product_name': 'Samsung Galaxy C23 Ultra', "
                           "'product_description': '256GB, Серый цвет, 200MP камера', '_Product__product_price': "
                           "180000.0, 'product_quantity': 5, 'performance': 500, 'model': 'Samsung Galaxy', "
                           "'memory': '256GB', 'color': 'Серый'}>, 1]], 'order_number': 2, 'product_total': 1, "
                           "'cost': 180000.0}>")


def test_order_add_product_in_list(smartphone_samsung, lw_dreams, smartphone_samsung0):
    order = Order()
    order.add_product_in_list(smartphone_samsung)
    assert order.product_list == ("[<<class 'data.classes.Smartphone'>, {'product_name': 'Samsung Galaxy C23 Ultra', "
                                  "'product_description': '256GB, Серый цвет, 200MP камера', "
                                  "'_Product__product_price': 180000.0, 'product_quantity': 5, 'performance': 500, "
                                  "'model': 'Samsung Galaxy', 'memory': '256GB', 'color': 'Серый'}>, 1]")
    order.add_product_in_list(lw_dreams, 3)
    assert order.product_list == ("[<<class 'data.classes.Smartphone'>, {'product_name': 'Samsung Galaxy C23 Ultra', "
                                  "'product_description': '256GB, Серый цвет, 200MP камера', "
                                  "'_Product__product_price': 180000.0, 'product_quantity': 5, 'performance': 500, "
                                  "'model': 'Samsung Galaxy', 'memory': '256GB', 'color': 'Серый'}>, 1][<<class "
                                  "'data.classes.LawnGrass'>, {'product_name': 'Мечта садовника', "
                                  "'product_description': 'Неприхотлива', '_Product__product_price': 1230.0, "
                                  "'product_quantity': 17, 'country': 'Россия', 'germ_period': 20, "
                                  "'color': 'зеленая'}>, 3]")

    assert order.add_product_in_list(smartphone_samsung0, 3) == "You can't add a product with 0 quantity"


def test_add_prod_0(smartphone_new_samsung_0, lw_new_0, tv_new_0):
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        Smartphone.add_product(*smartphone_new_samsung_0)
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        Product.add_product(*tv_new_0)
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        LawnGrass.add_product(*lw_new_0)


def test_get_average_price(smartphone, smartphone1, category_tv):
    assert smartphone.get_average_price() == 180000.0
    assert smartphone1.get_average_price() == 140000.0
    assert category_tv.get_average_price() == 0
