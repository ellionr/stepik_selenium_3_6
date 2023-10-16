import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    browser.get(f'https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')
    yield browser
    browser.quit()
