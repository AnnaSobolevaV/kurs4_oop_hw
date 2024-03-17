class Category:
    '''
    Класс "Категоря" (Category) содержит атрибуты:
    - category_name - название категории
    - category_description - опиcание категории
    - product_list - список товаров в категории
    - category_total - счетчик категорий
    - product_total - счетчик товаров
    '''
    category_name: str
    category_description: str
    product_list: list
    category_total = 0
    product_total = 0

    def __init__(self, category_name, category_description, product_list):
        self.category_name = category_name
        self.category_description = category_description
        self.product_list = product_list
        Category.category_total += 1
        Category.product_total += len(product_list)


class Product:
    '''
    Класс "Продукт" (Product) содержит:
    - product_name - название товара
    - product_description - опиcание товара
    - product_price - цена товара
    - product_quantity - количество товаров в наличии
    '''
    product_name: str
    product_description: str
    product_price: float
    product_quantity: int

    def __init__(self, product_name, product_description, product_price, product_quantity):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_quantity = product_quantity
