from page.HomePage import HomePage
from Tests.conftest import BaseTest
from utilities.custom_logger import LogGen


class TestWeb(BaseTest):
    """Each method is a test case"""
    # __test__ = False

    logger = LogGen.log_gen()
    logger.info("********** Web UI Automation **********")

    def test_job_type_test(self):
        """Search for job title 'Test' and verify the result for 'Netherlands' location"""
        job = 'test'
        country = 'Netherlands'
        self.homePage = HomePage(self.driver)
        self.homePage.allow_cookies()
        self.homePage.enter_job_search(job)
        self.homePage.click_search_button()
        assert self.homePage.search_result_text() == 'Showing Search results for "{0}"'.format(job), "Job search is not matched"
        assert self.homePage.verify_job_location() == True, f'Location should be vary'
        self.homePage.click_country_option(country)
        assert self.homePage.get_tag_text(country) == True, "Country name not find"
        assert all(element == country for element in self.homePage.verify_job_listing_by(country)) == True, \
            f"Location must be matched"

    def test_job_type_sales(self):
        """Search for job title 'Sales' and verify the result for 'Germany' location"""
        job = 'Sales'
        country = 'Germany'
        self.homePage = HomePage(self.driver)
        self.homePage.scroll_to_search()
        self.homePage.enter_job_search(job)
        self.homePage.click_search_button()
        assert self.homePage.search_result_text() == 'Showing Search results for "{0}"'.format(job), "Job search is not matched"
        assert all(element == job for element in self.homePage.verify_job(job)) == True, \
            f"Job title must be matched"
        self.homePage.click_country_option(country)
        assert self.homePage.get_tag_text(country) == True, "Country name not find"
        assert all(element == country for element in self.homePage.verify_job_listing_by(country)) == True, \
            f"Location must be matched"
