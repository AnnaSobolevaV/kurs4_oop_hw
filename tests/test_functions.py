from utils import functions
from utils.functions import load_data
import pytest


def test_load_data_empty():
    assert functions.load_data('') == None


def test_load_data():
    assert functions.load_data('./tests/test1.json') == [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не только коммуникации, "
                               "но и получение дополнительных функций для удобства жизни",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                        "performance": 500,
                        "model": "Samsung Galaxy",
                        "memory": "256GB",
                        "color": "Серый"

                    }
                ]
            }
    ]


@pytest.fixture
def test_empty_data():
    data = load_data('./tests/test_empty_data.json')
    return data


@pytest.fixture
def test_data():
    data = load_data('./tests/test.json')
    return data


def test_to_create_list_of_categories_with_products(test_data, test_empty_data):
    assert functions.to_create_list_of_categories_with_products(test_empty_data) == []
    assert type(functions.to_create_list_of_categories_with_products(test_data)) == list
