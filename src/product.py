from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(other) == type(self):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError

    @classmethod
    def new_product(cls, dict_of_product: dict):
        name = dict_of_product.get('name')
        description = dict_of_product.get('description')
        price = dict_of_product.get('price')
        quantity = dict_of_product.get('quantity')
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        else:
            self.__price = new_price


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products, total_quantity=0):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
        self.total_quantity = total_quantity

    def __str__(self):
        if self.name == 'Смартфоны':
            for product in self.__products:
                self.total_quantity += product.quantity
            return f'{self.name}, количество продуктов: {self.total_quantity} шт.'
        else:
            return 'Другая категория'

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ''
        for product in self.__products:
            product_str += f'{str(product)}\n'
        return product_str

    @property
    def products_in_list(self):
        return self.__products


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)  # 2 580 000
    print(product1 + product3)  # 1 334 000
    print(product2 + product3)  # 2 114 000
