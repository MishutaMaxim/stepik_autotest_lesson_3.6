import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем опцию с языком для запуска, параметр по умолчанию ru
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")

# Объявляем фикстуру для теста
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language") # Получили пользовательский язык и записали в переменную
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) # Передали опцию с языком браузера
    browser = webdriver.Chrome(options=options) # Объявили сам браузер
    yield browser
    browser.quit() # Закрыли браузер после теста
