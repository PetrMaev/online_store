import pytest

from src.product import Category, Product


@pytest.fixture
def product_for_test():
    return Product(
        name='Стул',
        description='Деревянный, для кухни',
        price=1000.0,
        quantity=4
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
