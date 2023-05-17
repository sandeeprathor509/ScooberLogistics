import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).click()

    def element_click(self, locator, element):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((locator, element))).click()

    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_up(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(Keys.CONTROL + Keys.HOME)

    def element_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        return element.is_enabled()

    def get_title(self, title):
        WebDriverWait(self.driver, 3).until(EC.title_is(title))
        return self.driver.title

    def element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except Exception as e:
            return False

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 700)")

    def scroll_up(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def job_lists(self, by_locator):
        location = []
        try:
            for i in range(1, 11):
                element = WebDriverWait(self.driver, 3).until(
                    EC.visibility_of_element_located((By.XPATH, by_locator.format(i))))
                if element.is_displayed():
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    location.append(element.text)
                else:
                    break
            return location
        except Exception as e:
            return location
