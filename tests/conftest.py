import pytest

from src.product import Category, Product
from src.product_categories import Smartphone, LawnGrass


@pytest.fixture
def product_for_test():
    return Product(
        name='Стул',
        description='Деревянный, для кухни',
        price=1000.0,
        quantity=4
    )


@pytest.fixture
def product_for_test_2():
    return Product(
        name='Стол',
        description='Круглый, белый',
        price=5000.0,
        quantity=3
    )


@pytest.fixture
def first_category():
    return Category(
        name='Мебель',
        description='Мебель не только для комфорта, но и часть стильного дизайна',
        products=[
            Product(name='Стул', description='Деревянный, для кухни', price=1000.0, quantity=4),
            Product(name='Стол', description='Круглый, белый', price=5000.0, quantity=3)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name='Посуда',
        description='Посуда, которая дарит радость',
        products=[
            Product(name='Чашка', description='Большая, белая', price=300.0, quantity=16),
            Product(name='Ложка', description='Чайная, гравированная', price=200.0, quantity=27)
        ]
    )


@pytest.fixture
def first_category_phones():
    return Category(
        name='Смартфоны',
        description='Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни',
        products=[
            Product(name='Nokia 3210', description='Неубиваемый', price=1000.0, quantity=4),
            Product(name='Motorolla C115', description='Круглый корпус', price=2000.0, quantity=3)
        ]
    )


@pytest.fixture
def first_product_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture
def second_product_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def first_product_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def second_product_grass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_without_price():
    return Category(
        name='Мебель',
        description='Мебель не только для комфорта, но и часть стильного дизайна',
        products=[
            Product(name='Стул', description='Деревянный, для кухни', price=0, quantity=4),
            Product(name='Стол', description='Круглый, белый', price=0, quantity=3)
        ]
    )
