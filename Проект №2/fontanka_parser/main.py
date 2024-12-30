from fontanka_parser.scheduler import NewsScheduler
from fontanka_parser.config import get_config

def main():
    """
    Запускает планировщик задач для парсинга новостей.
    Также выводит сводку новостей сразу после запуска программы.
    """
    try:
        config = get_config()
        summary_time = config.get("summary_time", "19:00")

        scheduler = NewsScheduler(summary_time=summary_time)

        # Вывод сводки новостей сразу после запуска
        scheduler.daily_summary()

        # Запуск планировщика задач
        scheduler.start()
    except KeyboardInterrupt:
        print("\nПрограмма была прервана пользователем.")

if __name__ == "__main__":
    main()
