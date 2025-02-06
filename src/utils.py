import json
import os
from typing import Any

from config import PATH_TO_PRODUCTS
from src.product import Product, Category


def read_json(path_to_file: str) -> dict[str, Any]:
    """ Считывает данные из JSON файла """
    full_path = os.path.abspath(path_to_file)
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict[str, Any]) -> list:
    """ Подгрузка данных по категориям и товарам из файла JSON """
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))
    return categories


if __name__ == '__main__':
    products_list = read_json(PATH_TO_PRODUCTS)
    products_data = create_objects_from_json(products_list)
    print(products_data[0].name)
    print(products_data[0].products)
    print(products_data[1].name)
    print(products_data[1].products)
