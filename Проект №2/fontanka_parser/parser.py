"""
Содержит класс для парсинга новостей с сайта fontanka.ru для города Санкт-Петербург.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from utils.validation import validate_news_data
from utils.exceptions import InvalidDataFormat

class NewsParser:
    """
    Класс для парсинга новостей с сайта fontanka.ru для Санкт-Петербурга.
    """

    def __init__(self, base_url: str = "https://www.fontanka.ru/spb/"):
        """
        Инициализирует объект парсера с базовым URL.
        :param base_url: Базовый URL для парсинга новостей (по умолчанию СПб).
        :raises ValueError: Если base_url некорректен.
        """
        if not base_url.startswith("http"):
            raise ValueError(f"Некорректный URL: {base_url}")
        self.base_url = base_url

    def fetch_page(self) -> str:
        """
        Получает HTML-код страницы.
        :return: HTML-код страницы.
        :raises requests.RequestException: Если запрос завершился с ошибкой.
        """
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise requests.RequestException(f"Ошибка при запросе: {e}")

    def parse_news(self, html: str) -> list:
        """
        Парсит новости за сегодняшний день из HTML-кода страницы.
        :param html: HTML-код страницы.
        :return: Список новостей в формате словаря.
        :raises InvalidDataFormat: Если структура данных некорректна.
        """
        soup = BeautifulSoup(html, 'html.parser')
        news_items = []
        today = datetime.now().strftime("%d.%m.%Y")

        for article in soup.find_all('li', class_='IZagl L7br'):
            try:
                # Дата новости
                date_tag = article.find('time', class_='IZdx')
                date = date_tag.find('span').text.strip() if date_tag else ""
                if not today in date:
                    continue

                # Заголовок и ссылка
                title_tag = article.find('a', class_='IZcp')
                title = title_tag.text.strip() if title_tag else ""
                link = title_tag['href'] if title_tag else ""

                news_data = {
                    'title': title,
                    'link': f"https://www.fontanka.ru{link}" if link.startswith('/') else link,
                    'timestamp': date,
                }
                validate_news_data(news_data)
                news_items.append(news_data)

            except (AttributeError, TypeError, KeyError):
                continue

        # Вывод в консоль в обратном порядке
        for news in reversed(news_items):
            print(f"Заголовок: {news['title']}\nСсылка: {news['link']}\n")

        return news_items
