import json
from data import classes


def load_data(file_json):
    """
    Загружает данные из файла json
    """
    if file_json != '':
        with open(file_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data


def to_create_list_of_categories_with_products(data):
    categories = []
    for item in data:
        product_list = []

        products = item.get('products')
        for product in products:
            product_list.append(classes.Product(product['name'],
                                                product['description'], product['price'], product['quantity']))
        category = classes.Category(item.get('name'), item.get('description'), product_list)
        categories.append(category)
    return categories
