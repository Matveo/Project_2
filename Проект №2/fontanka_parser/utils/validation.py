"""
Содержит функции для валидации данных, включая проверки формата времени, структуры новостей и JSON.
"""

import re
from .exceptions import InvalidTimeFormat, InvalidDataFormat, JSONValidationError

def validate_time_format(time_str: str) -> None:
    """
    Проверяет, что время задано в формате HH:MM и находится в допустимых пределах.
    :param time_str: строка времени (например, "19:00")
    :raises InvalidTimeFormat: если формат времени некорректен.
    """
    if not re.match(r'^([01]?\d|2[0-3]):([0-5]?\d)$', time_str):
        raise InvalidTimeFormat(f"Некорректный формат времени: {time_str}")

def validate_news_data(news_data: dict) -> None:
    """
    Проверяет структуру данных новостей.
    Ожидается, что news_data содержит ключи 'title', 'link', 'timestamp'.
    :param news_data: словарь с данными новостей.
    :raises InvalidDataFormat: если структура некорректна.
    """
    required_keys = {'title', 'link', 'timestamp'}
    if not isinstance(news_data, dict):
        raise InvalidDataFormat("Данные новостей должны быть словарём.")
    if not required_keys.issubset(news_data.keys()):
        raise InvalidDataFormat(f"Данные новостей должны содержать ключи: {', '.join(required_keys)}")

def validate_json_structure(data: list) -> None:
    """
    Проверяет, что данные для сохранения в JSON имеют правильный формат.
    Ожидается список словарей с корректной структурой новостей.
    :param data: данные для проверки.
    :raises JSONValidationError: если структура некорректна.
    """
    if not isinstance(data, list):
        raise JSONValidationError("JSON должен быть списком новостей.")
    for item in data:
        validate_news_data(item)
