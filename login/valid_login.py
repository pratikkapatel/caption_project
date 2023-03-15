import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.browser_config import WebDriverWrapper
from utils import data_source

class TestAdd_HR(WebDriverWrapper):

    @pytest.mark.parametrize(
        "firstname, lastname, emailid, jobtitle, companyname, phonenum", data_source.test_add_valid_hr_data
    )

    def test_add_valid_HR(self, firstname, lastname, emailid, jobtitle,companyname, phonenum):
        self.driver.find_element(By.XPATH,"(//a[normalize-space()='Try It Free'])").click()
        #time.sleep(5)
        self.driver.find_element(By.ID, "FirstName").send_keys(firstname)
        self.driver.find_element(By.ID, "LastName").send_keys(lastname)
        self.driver.find_element(By.ID, "Email").send_keys(emailid)
        self.driver.find_element(By.ID, "Title").send_keys(jobtitle)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.ID, "Company").send_keys(companyname)
        self.driver.find_element(By.ID, "Phone").send_keys(phonenum)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, "(//select[@id='Employees_Text__c'])[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "// option[ @ value = '25-75']").click()
        self.driver.find_element(By.XPATH, "//select[@id='Country']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//option[@value='India']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Get Free Trial']").click()