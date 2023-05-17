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
