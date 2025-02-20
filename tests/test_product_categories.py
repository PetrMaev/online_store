import pytest

def test_product_smartphone_init(first_product_smartphone):
    assert first_product_smartphone.name == 'Samsung Galaxy S23 Ultra'
    assert first_product_smartphone.description == '256GB, Серый цвет, 200MP камера'
    assert first_product_smartphone.price == 180000.0
    assert first_product_smartphone.quantity == 5
    assert first_product_smartphone.efficiency == 95.5
    assert first_product_smartphone.model == 'S23 Ultra'
    assert first_product_smartphone.memory == 256
    assert first_product_smartphone.color == 'Серый'


def test_product_smartphone_add(first_product_smartphone, second_product_smartphone):
    assert first_product_smartphone + second_product_smartphone == 2580000.0


def test_product_smartphone_add_error(first_product_smartphone):
    with pytest.raises(TypeError):
        result = first_product_smartphone + 1


def test_product_grass_init(first_product_grass):
    assert first_product_grass.name == 'Газонная трава'
    assert first_product_grass.description == 'Элитная трава для газона'
    assert first_product_grass.price == 500.0
    assert first_product_grass.quantity == 20
    assert first_product_grass.country == 'Россия'
    assert first_product_grass.germination_period == '7 дней'
    assert first_product_grass.color == 'Зеленый'


def test_product_grass_add(first_product_grass, second_product_grass):
    assert first_product_grass + second_product_grass == 35


def test_product_grass_add_error(first_product_grass):
   with pytest.raises(TypeError):
       result = first_product_grass + 1
