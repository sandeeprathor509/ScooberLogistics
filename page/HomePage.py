import time
from selenium.webdriver.common.by import By
from page.BasePage import BasePage


class HomePage(BasePage):
    """By locators"""
    job_search = (By.ID, "keywordSearch")
    search_button = (By.ID, "ph-search-backdrop")
    company_logo = (By.XPATH, "(//img[@alt='Company Logo'])[1]")
    location_list = "(//span[@class='job-location'])[{0}]"
    job_title = "(//div[@class='job-title'])[{0}]"
    country = (By.XPATH, "//button[@id='CountryAccordion']/i")
    category = (By.XPATH, "//button[@id='CategoryAccordion']/i")
    type_category = (By.XPATH, "//input[@id='facetInput_0']")
    category_result = (By.XPATH, "(//span[@class='result-text'])[1]")
    type_country = (By.XPATH, "//input[@id='facetInput_1']")
    country_result = "//span[contains(text(),'{0}')]"
    allow_cookies_option = (By.XPATH, "//button[@click.delegate='acceptAndClose()']")
    search_result = (By.XPATH, "//h2[@show.bind='searchKeyword']")
    tag_after_country_select = (By.XPATH, "//li[@class='tag']/span")
    job_counter = "(//li[@role='presentation'])[{0}]"

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """verify the title of the page"""

    def get_page_title(self, page_title):
        return self.get_title(page_title)

    """use to enter the job title in the page"""

    def enter_job_search(self, job_title):
        self.do_send_keys(self.job_search, job_title)

    def click_search_button(self):
        self.do_click(self.search_button)

    def verify_visibility_of_company_logo(self):
        self.element_displayed(self.company_logo)

    def scrolling_down(self):
        self.scroll_down()

    def scroll_to_search(self):
        self.scroll_to_up(self.search_button)

    def verify_job_location(self):
        job_location = self.job_lists(self.location_list)
        location_set = set(job_location)
        if len(location_set) < 3:
            return False
        else:
            return True

    def click_country_option(self, country):
        self.scroll_to_element(self.search_button)
        self.do_click(self.country)
        self.do_send_keys(self.type_country, country)
        self.element_click(By.XPATH, self.country_result.format(country))
        time.sleep(2)

    def verify_job_listing_by(self, search_type):
        job_listing = self.job_lists(self.location_list)
        return_list = []
        for i in range(len(job_listing)):
            if self.extract_word(job_listing[i]) == search_type:
                return_list.append(self.extract_word(job_listing[i]))
            else:
                return_list.append("False")

        return return_list

    def verify_job(self, search_type):
        jobs = self.job_lists(self.job_title)
        return_job = []
        for i in range(len(jobs)):
            if self.extract_job(jobs[i], search_type) == search_type:
                return_job.append(search_type)
            else:
                return_job.append("False")

        return return_job

    def extract_word(self, string):
        parts = string.split("\n")
        last_part = parts[-1]
        last_part = last_part.strip()
        word = last_part.split()[-1]
        return word

    def extract_job(self, string, job):
        parts = string.split()
        for part in parts:
            if job in part:
                result = job
                break
        else:
            result = None

        return result

    def allow_cookies(self):
        self.do_click(self.allow_cookies_option)

    def search_result_text(self):
        self.scroll_to_element(self.search_result)
        return self.get_text(self.search_result)

    def get_tag_text(self, country):
        self.scroll_to_element(self.tag_after_country_select)
        if self.get_text(self.tag_after_country_select) == country:
            return True
        else:
            return False