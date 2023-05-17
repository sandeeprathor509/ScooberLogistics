import unittest

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from Conf.configurationtest import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    @pytest.fixture(scope='class')
    def init_driver(self, request):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())
        driver.maximize_window()
        driver.get(TestData.URL)
        request.cls.driver = driver
        yield
        driver.close()

# @pytest.fixture
# def config(request, scope='session'):
#     BROWSERS = ['Chrome', 'Firefox']
#
#     # Read config file
#     with open('../../config.json') as config_file:
#         config = json.load(config_file)
#
#     browser = request.config.option.browser
#     if browser is not None:
#         config['browser'] = browser
#
#     # Assert values are acceptable
#     assert config['browser'] in BROWSERS
#     assert isinstance(config['implicit_wait'], int)
#     assert config['implicit_wait'] > 0
#
#     # Return config so it can be used
#     return config
#
#
# @pytest.fixture(params=['chrome'], scope='class')
# def setup_ui(config):
#     global WEB_DRIVER
#     if config['browser'] == 'Chrome':
#         opts = webdriver.ChromeOptions()
#         WEB_DRIVER = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
#     elif config['browser'] == 'Firefox':
#         opts = webdriver.FirefoxOptions()
#         WEB_DRIVER = webdriver.Firefox(GeckoDriverManager().install(), options=opts)
#     else:
#         raise Exception(f'Browser "{config["browser"]}" is not supported')
#
#     WEB_DRIVER.maximize_window()
#     WEB_DRIVER.implicitly_wait(config['implicit_wait'])
#     #WEB_DRIVER.get(TestData.URL)
#
#     yield WEB_DRIVER
#
#     WEB_DRIVER.quit()
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store")
#
#
# @pytest.fixture
# def browser(config):
#     # Initialize the WebDriver instance
#     if config['browser'] == 'Chrome':
#         opts = webdriver.ChromeOptions()
#         b = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
#     elif config['browser'] == 'Firefox':
#         opts = webdriver.FirefoxOptions()
#         b = webdriver.Firefox(GeckoDriverManager().install(), options=opts)
#     else:
#         raise Exception(f'Browser "{config["browser"]}" is not supported')
#
#     # Make call wait up to 10 seconds for elements to appear
#     b.implicitly_wait(config['implicit_wait'])
#
#     # Return the WebDriver instance for the setup
#     yield b
#
#     # Quit the WebDriver instance for the teardown
#     b.quit()
#
#
# @pytest.fixture
# def datatable():
#     return DataTable()
#
#
# class DataTable(object):
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         dt_str = ''
#         for field, value in self.__dict__.items():
#             dt_str = f'{dt_str}\n{field} = {value}'
#         return dt_str
#
#     def __repr__(self) -> str:
#         return self.__str__()
#
#
# @given(parsers.parse('Navigate to the JET career page'), target_fixture='launch_browser')
# def launch_browser(browser):
#     browser.get(TestData.URL)
