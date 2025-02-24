from src.product import Product, Category
from src.product_categories import Smartphone, LawnGrass


def test_print_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Iphone 15, 512GB, Gray space, 210000.0, 8)'

    Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    message = capsys.readouterr()
    assert message.out.strip() == 'Smartphone(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)'

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)'
