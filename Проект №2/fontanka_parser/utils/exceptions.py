"""
Содержит пользовательские исключения для обработки ошибок валидации и данных.
"""

class InvalidTimeFormat(Exception):
    """Исключение для некорректного формата времени."""
    pass

class InvalidDataFormat(Exception):
    """Исключение для некорректной структуры данных новостей."""
    pass

class JSONValidationError(Exception):
    """Исключение для ошибок структуры данных JSON."""
    pass
