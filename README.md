Lesson 10 — PageObject + Allure

В данном разделе реализованы автоматизированные тесты с использованием Selenium WebDriver, паттерна PageObject и системы отчетов Allure.
Каждое задание вынесено в отдельную папку.

Используемые технологии:
Python 3.10+
Selenium WebDriver
Pytest
Allure (allure-pytest)
PageObject pattern

Установка зависимостей:
Создать и активировать виртуальное окружение:
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows


Установить зависимости:
pip install selenium pytest allure-pytest

Установить Allure CLI:
Linux / macOS

brew install allure

Windows
Скачать с официальной документации Allure и добавить в PATH.

Запуск тестов с формированием отчета Allure
Задание 1 — Форма
pytest task_01 --alluredir=task_01/allure-results

Задание 2 — Калькулятор
pytest task_02 --alluredir=task_02/allure-results

Задание 3 — Магазин (SauceDemo)
pytest task_03 --alluredir=task_03/allure-results

Просмотр отчета Allure

Для просмотра отчета используйте команду:

allure serve <путь_к_allure-results>

Примеры:

allure serve lesson_10/task_01/allure-results
allure serve lesson_10/task_02/allure-results
allure serve lesson_10/task_03/allure-results


После выполнения команды отчет автоматически откроется в браузере.

