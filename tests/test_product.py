def test_product(product_for_test):
    assert product_for_test.name == 'Стул'
    assert product_for_test.description == 'Деревянный, для кухни'
    assert product_for_test.price == 1000.0
    assert product_for_test.quantity == 4


def test_category(first_category, second_category):
    assert first_category.name == 'Мебель'
    assert first_category.description == 'Мебель не только для комфорта, но и часть стильного дизайна'
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_product_list_property(first_category):
    assert first_category.products == ('Стул, 1000.0 руб. Остаток: 4 шт.\n'
                                       'Стол, 5000.0 руб. Остаток: 3 шт.\n')


def test_product_list_setter(first_category, product_for_test):
    assert len(first_category.products_in_list) == 2
    first_category.add_product(product_for_test)
    assert len(first_category.products_in_list) == 3


def test_price_property(product_for_test):
    assert product_for_test.price == 1000


def test_product_str(product_for_test):
    assert str(product_for_test) == 'Стул, 1000.0 руб. Остаток: 4 шт.'


def test_category_str(first_category):
    assert str(first_category) == 'Другая категория'


def test_category_str_2(first_category_phones):
    assert str(first_category_phones) == 'Смартфоны, количество продуктов: 7 шт.'


def test_product_add(product_for_test, product_for_test_2):
    assert product_for_test + product_for_test_2 == 19000
