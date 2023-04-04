import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://demowebshop.tricentis.com/")
        logo = self.driver.find_element(By.XPATH, "//img[@alt='Tricentis Demo Web Shop']").is_displayed()
        if logo == True:
            assert True
        else:
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.skip
    def test_listofallemployees(self):
        pytest.skip("skipping test..will implement later")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "OrangeHRM123":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="Login screen",attachment_type=AttachmentType.PNG)
            assert False





