class Category:
    """
    Класс "Категория" (Category) содержит атрибуты:
    - category_name - название категории
    - category_description - опиcание категории
    - product_list - список товаров в категории
    - category_total - счетчик категорий
    - product_total - счетчик товаров
    """
    category_name: str
    category_description: str
    __product_list: list
    category_total = 0
    product_total = 0

    def __init__(self, category_name, category_description, product_list):
        self.category_name = category_name
        self.category_description = category_description
        self.__product_list = product_list
        Category.category_total += 1
        Category.product_total += len(self.__product_list)

    def __str__(self):
        return (f'{self.category_name}, количество продуктов: {len(self)} шт.\n'
                f'{self.product_list}')

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.category_name}', '{self.category_description}', {self.__product_list})"
            f"{self.category_total}, {self.product_total}"
        )

    def __len__(self):
        total_prod_in_category = 0
        for prod in self.__product_list:
            total_prod_in_category += prod.product_quantity
        return total_prod_in_category

    @property
    def product_list(self):
        products_printed = ''
        for prod in self.__product_list:
            products_printed += str(prod)
        return products_printed

    def add_product_in_list(self, new_prod):
        self.__product_list.append(new_prod)


class Product:
    """
    Класс "Продукт" (Product) содержит:
    - product_name - название товара
    - product_description - опиcание товара
    - product_price - цена товара
    - product_quantity - количество товаров в наличии
    """
    product_name: str
    product_description: str
    __product_price: float
    product_quantity: int

    def __init__(self, prod_name, prod_description, prod_price, prod_quantity):
        self.product_name = prod_name
        self.product_description = prod_description
        self.__product_price = prod_price
        self.product_quantity = prod_quantity

    def __str__(self):
        return (f'{self.product_name}, {self.product_price} руб. Остаток: {self.product_quantity} шт.\n')

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.product_name}', '{self.product_description}',"
                f" {self.product_price}, {self.product_quantity})")

    def __len__(self):
        return self.product_quantity

    def __add__(self, other):
        return self.product_price * len(self) + other.product_price * len(other)

    @classmethod
    def add_product(cls, *arg):
        prod_name, prod_description, prod_price, prod_quantity = arg
        new_prod = Product(prod_name, prod_description, prod_price, prod_quantity)
        return new_prod

    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, new_price):
        if new_price <= 0:
            print('ERROR: Введена некорректная цена. Цена должна быть больше 0')
        else:
            self.__product_price = float(new_price)
