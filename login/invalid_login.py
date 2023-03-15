import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.browser_config import WebDriverWrapper
from utils import data_source


class TestLogin(WebDriverWrapper):
    def test_invalid_login(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Log In']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//input[@id='domain']").send_keys("einfochips")
        self.driver.find_element(By.ID, "submit").click()
        actual_text = self.driver.find_element(By.XPATH, "(//span[@class='hI9SEurDvDymAAD3fEZKBA=='])[1]").text
        assert_that("That doesn't look like").contains(actual_text)

    @pytest.mark.parametrize("domain, expected_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, domain, expected_error):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Log In']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//input[@id='domain']").send_keys(domain)
        self.driver.find_element(By.ID, "submit").click()
        actual_error = self.driver.find_element(By.XPATH, "(//span[@class='hI9SEurDvDymAAD3fEZKBA=='])[1]").text
        print(actual_error)
        assert_that(expected_error).contains(actual_error)