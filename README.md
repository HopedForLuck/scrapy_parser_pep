# Проект создания парсера PEP с использованием фреймворка Scrapy

## Описание

scrapy_parser_pep - проект по созданию парсера, собирающего все PEP с официального сайта документация и создающий два файла:
- Файл содержащий общее количество PEP и количество по каждому статусу
- Файл содержащий номер, название и статус каждого PEP

В проекте настроен вывод в .csv файлы с указанием даты и времени создания файла в названии

## Стек

- Python
- Scrapy

## Настройка проекта

- Клонировать репозиторий

```bash
git clone
```

- Установить и активировать виртуальное окружение

```bash
python -m venv venv (для Windows)
python3 -m venv venv (для Linux)
```

```bash
source venv/Scripts/activate (для Windows)
source venv/bin/activate (для Linux)
```

```bash
python -m pip install --upgrade pip (для Windows)
python3 -m pip install --upgrade pip (для Linux)
```

- Установить зависимости из файла requirements.txt

```bash
pip install -r requirements.txt
```

## Автор проекта:

##### Чурилов Александр - [https://github.com/HopedForLuck]
