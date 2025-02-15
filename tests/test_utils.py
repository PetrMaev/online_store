from unittest.mock import patch, mock_open

from config import PATH_TO_PRODUCTS
from src.utils import read_json, create_objects_from_json


def test_read_json():
    mocked_open = mock_open(read_data=r'{"name": "55\" QLED 4K", "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}')

    with patch('builtins.open', mocked_open):
        result = read_json(PATH_TO_PRODUCTS)
        assert result == {"name": "55\" QLED 4K", "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
