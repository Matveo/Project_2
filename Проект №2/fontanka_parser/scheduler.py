"""
Содержит планировщик задач для регулярной отправки сводки новостей.
"""

import schedule
import time
import logging
from datetime import datetime
from parser import NewsParser
from utils.json_helper import save_to_json
from utils.validation import validate_time_format

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class NewsScheduler:
    """
    Класс для планирования задач по сбору и сохранению новостей.
    """

    def __init__(self, summary_time: str = "19:00"):
        """
        Инициализация планировщика.
        :param summary_time: Время (HH:MM), когда выполняется сбор новостей.
        :raises ValueError: Если время некорректно.
        """
        validate_time_format(summary_time)
        self.summary_time = summary_time
        self.parser = NewsParser()

    def daily_summary(self):
        """
        Ежедневный сбор и сохранение новостей за текущий день.
        """
        logging.info("Начинается сбор новостей за сегодняшний день.")
        html = self.parser.fetch_page()
        news = self.parser.parse_news(html)

        if news:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"news_summary_{timestamp}.json"
            save_to_json(news, file_name)
        else:
            logging.info("Новостей за сегодняшний день не найдено.")

    def start(self):
        """
        Запуск планировщика задач.
        """
        schedule.every().day.at(self.summary_time).do(self.daily_summary)
        logging.info(f"Планировщик задач запущен. Сводка будет собираться в {self.summary_time}.")

        while True:
            schedule.run_pending()
            time.sleep(1)
