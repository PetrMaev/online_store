def test_product(product_for_test):
    assert product_for_test.name == 'Стул'
    assert product_for_test.description == 'Деревянный, для кухни'
    assert product_for_test.price == 1000.0
    assert product_for_test.quantity == 4


def test_category(first_category, second_category):
    assert first_category.name == 'Мебель'
    assert first_category.description == 'Мебель не только для комфорта, но и часть стильного дизайна'
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4
