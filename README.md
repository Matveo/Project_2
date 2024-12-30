# Проект №2

## Авторы проекта
Виноградская Серафима Дмитриевна ИСУ: 465404
Бровкин Матвей Вадимович ИСУ: 465283

## О проекте
Проект представляет собой бота для ежедневного парсинга новостей с сайта [fontanka.ru](https://www.fontanka.ru/) по городу Санкт-Петербург. Бот собирает последние новости за текущий день, выводит их в консоль и сохраняет в JSON-файл. По умолчанию бот собирает сводку новостей в 19:00 по московскому времени, но также выводит новости сразу после запуска.

## Примеры использования

### Запуск проекта
Для запуска бота выполните команду:

```bash
python main.py
```

### Пример вывода в консоли

После запуска бот выведет заголовки и ссылки на новости за текущий день:

```
Заголовок: В Петербурге запретили выходить на лед
Ссылка: https://www.fontanka.ru/2024/12/29/74945348/

Заголовок: В Консерватории Римского-Корсакова зазвучала музыка. Впервые за 10 лет
Ссылка: https://www.fontanka.ru/2024/12/29/74945732/
```

### Файлы JSON

Каждая сводка сохраняется в JSON-файл с именем формата `news_summary_YYYY-MM-DD_HH-MM-SS.json`. Пример содержимого файла:

```json
[
    {
        "title": "В Петербурге запретили выходить на лед",
        "link": "https://www.fontanka.ru/2024/12/29/74945348/",
        "timestamp": "29.12.2024"
    },
    {
        "title": "В Консерватории Римского-Корсакова зазвучала музыка. Впервые за 10 лет",
        "link": "https://www.fontanka.ru/2024/12/29/74945732/",
        "timestamp": "29.12.2024"
    }
]
```

### Изменение настроек
Настройки бота находятся в файле `config.py`. Вы можете изменить время выполнения ежедневной сводки, указав время в формате `HH:MM`:

```python
{
    "summary_time": "18:00"
}
```

## Поддержка и помощь
В процессе разработки проекта немного использовались возможности ChatGPT 4.0. Модель помогала:
- Писать понятные комментарии и док-строки;
- Исправлять ошибки в коде;
- Улучшать читаемость и стиль кода в соответствии с PEP 8;
- Оптимизировать решение для повышения читаемости и удобства работы с проектом.

## Разделение обязанностей
- За идею проекта и файлы из папки utils отвечала Серафима
- За файлы config, init, main, parser, scheduler отвечал Матвей
