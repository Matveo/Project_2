"""
Содержит функции для работы с JSON-файлами.
"""

import json
import logging
from utils.exceptions import JSONValidationError

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def save_to_json(data: list, file_name: str) -> None:
    """
    Сохраняет данные в JSON-файл.
    :param data: Данные для сохранения (список словарей).
    :param file_name: Имя файла для сохранения.
    :raises JSONValidationError: Если данные некорректны.
    """
    if not isinstance(data, list):
        raise JSONValidationError("Данные для сохранения должны быть списком.")

    try:
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        logging.info(f"Данные успешно сохранены в файл {file_name}.")
    except Exception as e:
        logging.error(f"Ошибка при сохранении данных в файл {file_name}: {e}")
        raise

def load_from_json(file_name: str) -> list:
    """
    Загружает данные из JSON-файла.
    :param file_name: Имя файла для загрузки.
    :return: Загруженные данные (список словарей).
    :raises JSONValidationError: Если файл содержит некорректные данные.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        if not isinstance(data, list):
            raise JSONValidationError("Загруженные данные должны быть списком.")
        logging.info(f"Данные успешно загружены из файла {file_name}.")
        return data
    except Exception as e:
        logging.error(f"Ошибка при загрузке данных из файла {file_name}: {e}")
        raise
