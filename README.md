# Парсер PEP документации на Python (Scrapy).

## Технологии:
[![Scrapy](https://camo.githubusercontent.com/40d00cefb120a829517e503658aaf6c987d5f9cc6be5e2e35fb20bd63bdbceb5/68747470733a2f2f7363726170792e6f72672f696d672f7363726170796c6f676f2e706e67)](https://scrapy.org/)

## Описание проекта:

#### Асинхронный Парсер позволяет получить актуальную информацию о статусах PEP — Python Enhancement Proposal, c возможностью сохранения работы парсера в формат .csv.

## Технические возможности парсера:
#### Парсер 'достаёт' информацию из списка статусов [PEP](https://peps.python.org/)(Номер PEP), далее переходит на страницы каждого PEP из списка, собирая информацию о статусе и названии PEP. 
#### Собирает все данные в pep_date_.csv (Номер PEP, Статус PEP, Название), также при работе автоматически формируется таблица  status_summary_date_.csv с Количеством PEP в каждом статусе, и общим количеством PEP.

## Запуск проекта:

#### Склонировать репозиторий:
> https://github.com/AntonDMoskalev/scrapy_parser_pep.git


#### Установить и активировать виртуальное окружение
> python -m venv venv

#### Обновить менеджер пакетов PIP
> python -m pip install --upgrade pip

#### Requirements.txt
> pip install -r requirements.txt

# Запустить парсер:
> scrapy crawl pep
