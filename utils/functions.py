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
    new_order = classes.Order()
    product_ = None
    for item in data:
        product_list = []
        products = item.get('products')
        for product in products:
            if item.get('name') == "Смартфоны":
                prod = classes.Smartphone(product['name'], product['description'], product['price'],
                                          product['quantity'],
                                          product['performance'], product['model'], product['memory'], product['color'])
                product_list.append(prod)
            elif item.get('name') == 'Трава газонная':
                prod = classes.LawnGrass(product['name'], product['description'], product['price'], product['quantity'],
                                         product['country'], product['germ_period'], product['color'])
                product_list.append(prod)
            else:
                prod = classes.Product(product['name'], product['description'], product['price'], product['quantity'])
                product_list.append(prod)
                product_ = prod
            print(prod.obj_creation_log())
        new_order.add_product_in_list(product_list[len(product_list) - 1], 2)
        print(new_order.obj_creation_log())
        category = classes.Category(item.get('name'), item.get('description'), product_list)
        categories.append(category)
        print(category.obj_creation_log())
    if product_ is not None:
        new_order = classes.Order()
        new_order.add_product_in_list(product_, 2)
        print(new_order.obj_creation_log())
    if product_ is not None:
        new_order = classes.Order()
        prod = classes.Product("Новый товар", 'description: "Новый товар"',
                               100, 0)
        new_order.add_product_in_list(prod, 2)
        print(new_order.obj_creation_log())

    return categories
