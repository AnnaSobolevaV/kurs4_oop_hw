from abc import ABC, abstractmethod


class MyException(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else 'Неизвестная ошибка.'

    def __str__(self):
        return self.message


class MixinLog:
    def __repr__(self):
        return f"<{self.__class__}, {self.__dict__}>"

    def obj_creation_log(self):
        return f'MixinLog: created: {self.__repr__()}'


class BaseClass(ABC):
    @abstractmethod
    def add_product_in_list(self, product):
        pass

    @staticmethod
    def check_quantity(product):
        if product.product_quantity == 0:
            raise MyException("You can't add a product with 0 quantity")


class Order(BaseClass, MixinLog):
    order_id = 0
    __product_list: list
    order_number: int
    product_total: int
    cost: float

    def __init__(self):
        self.__product_list = []
        self.order_number = Order.order_id + 1
        self.product_total = 0
        self.cost = 0
        Order.order_id += 1
        self.obj_creation_log()

    @property
    def product_list(self):
        products_printed = ''
        for prod in self.__product_list:
            products_printed += str(prod)
        return products_printed

    def add_product_in_list(self, product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError(f'{product.__class__} is not Product')
        else:
            try:
                super().check_quantity(product)
            except MyException as e:
                print(e)
                return str(e)
            else:
                self.__product_list.append([product, quantity])
                self.product_total += 1
                self.cost += quantity * product.product_price
                print("Продукт добавлен успешно")
                return f"{product.__class__} is added to Order №{self.order_number}"
            finally:
                print("Обработка добавления товара завершена")


class Category(BaseClass, MixinLog):
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
        if not isinstance(new_prod, Product):
            raise TypeError(f'{new_prod.__class__} is not Product')
        else:
            try:
                super().check_quantity(new_prod)
            except MyException as e:
                print(e)
                return str(e)
            else:
                self.__product_list.append(new_prod)
                print("Продукт добавлен успешно в Категорию")
                return f"{new_prod.__class__} is added to {self.category_name}"
            finally:
                print("Обработка добавления товара в Категорию завершена")

    def get_average_price(self):
        total_price = 0
        total_prod = 0
        try:
            for prod in self.__product_list:
                total_price += prod.product_price
                total_prod += 1
            return total_price / total_prod
        except ZeroDivisionError:
            return 0


class Things(ABC):
    @abstractmethod
    def add_product(self, new_prod):
        pass


class Product(Things, MixinLog):
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
        return f'{self.product_name}, {self.product_price} руб. Остаток: {self.product_quantity} шт.\n'

    def __len__(self):
        return self.product_quantity

    def __add__(self, other):
        if type(self) is type(other):
            return self.product_price * len(self) + other.product_price * len(other)
        else:
            raise TypeError("You can't add different classes")

    @classmethod
    def add_product(cls, *arg):
        prod_name, prod_description, prod_price, prod_quantity = arg
        if prod_quantity != 0:
            new_prod = Product(prod_name, prod_description, prod_price, prod_quantity)
            return new_prod
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')

    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, new_price):
        if new_price <= 0:
            print('ERROR: Введена некорректная цена. Цена должна быть больше 0')
        else:
            self.__product_price = float(new_price)


class Smartphone(Product):
    """
    Класс "Смартфоны" подкласс класса "Продукты"(Product) содержит:
    - performance: int - производительность
    - model: str - модель
    - memory: str - объем встроенной памяти
    - color: str - цвет
   """
    performance: int
    model: str
    memory: str
    color: str

    def __init__(self, prod_name, prod_description, prod_price, prod_quantity, performance, model, memory, color):
        super().__init__(prod_name, prod_description, prod_price, prod_quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def add_product(cls, *arg):
        prod_name, prod_description, prod_price, prod_quantity, performance, model, memory, color = arg
        if prod_quantity != 0:
            new_prod = Smartphone(prod_name, prod_description, prod_price, prod_quantity, performance, model, memory,
                                  color)
            return new_prod
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')


class LawnGrass(Product):
    """
    Класс "Трава газонная" подкласс класса "Продукты"(Product) содержит:
    - germ_period: str - страна-производитель
    - memory: str - срок прорастания
    - color: str - цвет
    """
    country: str
    germ_period: int
    color: str

    def __init__(self, prod_name, prod_description, prod_price, prod_quantity, country, germ_period, color):
        super().__init__(prod_name, prod_description, prod_price, prod_quantity)
        self.country = country
        self.germ_period = germ_period
        self.color = color

    @classmethod
    def add_product(cls, *arg):
        prod_name, prod_description, prod_price, prod_quantity, country, germ_period, color = arg
        if prod_quantity != 0:
            new_prod = LawnGrass(prod_name, prod_description, prod_price, prod_quantity, country, germ_period, color)
            return new_prod
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
