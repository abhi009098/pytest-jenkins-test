# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
#
#
# @pytest.fixture()
# def driver():
#     driver = webdriver.Edge()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

#
# @pytest.mark.parametrize("email,password,expected_result", [("jasonbourne@gmail.com", "tosca1234", "Log out"),("test@test.com", "password", "Log out")], ids=["valid credentials", "invalid credentials"])
# def test_login(driver, email, password, expected_result):
#     driver.get("https://demowebshop.tricentis.com/login")
#     driver.find_element(By.CSS_SELECTOR,"a.ico-login").click()
#     driver.find_element(By.CSS_SELECTOR,"#Email").send_keys(email)
#     driver.find_element(By.CSS_SELECTOR,"#Password").send_keys(password)
#     driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()
#     title = driver.find_element(By.CSS_SELECTOR,"a.ico-logout").text
#     assert title == expected_result,"successful login"
#     driver.find_element(By.CSS_SELECTOR, "a.ico-logout").click()


# def testfunction(driver):
#     driver.get("https://demowebshop.tricentis.com/login")
#     driver.find_element(By.CSS_SELECTOR,"a.ico-login").click()
#     driver.find_element(By.CSS_SELECTOR,"#Email").send_keys("jasonbourne@gmail.com")
#     driver.find_element(By.CSS_SELECTOR,"#Password").send_keys("tosca1234")
#     driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()
#     title = driver.find_element(By.CSS_SELECTOR,"a.ico-logout").text
#     assert title == "Log out","successful login"
#
#

# @pytest.mark.parametrize("email,password,expected_result", [("jasonbourne@gmail.com", "tosca1234", "Log out"),("test@test.com", "password", "Log in")], ids=["valid credentials", "invalid credentials"])
# def test_login(driver, email, password, expected_result):
#     driver.get("https://demowebshop.tricentis.com/login")
#     driver.find_element(By.CSS_SELECTOR,"a.ico-login").click()
#     driver.find_element(By.CSS_SELECTOR,"#Email").send_keys(email)
#     driver.find_element(By.CSS_SELECTOR,"#Password").send_keys(password)
#     driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()
#     if expected_result == 'Log out':
#         title = driver.find_element(By.CSS_SELECTOR,"a.ico-logout").text
#         assert title == expected_result,"successful login"
#         driver.find_element(By.CSS_SELECTOR, "a.ico-logout").click()
#     else:
#         print("invalid credentials given-Test was failed")
#         # with pytest.raises(NoSuchElementException):
#         #     driver.find_element(By.CSS_SELECTOR,"a.ico-logout").text
#
#
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture()
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_valid_credentials(driver):
    driver.get("https://demowebshop.tricentis.com/login")
    driver.find_element(By.CSS_SELECTOR,"a.ico-login").click()
    driver.find_element(By.CSS_SELECTOR,"#Email").send_keys("jasonbourne@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"#Password").send_keys("tosca1234")
    driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()
    title = driver.find_element(By.CSS_SELECTOR,"a.ico-logout").text
    assert title == "Log out","successful login"
    driver.find_element(By.CSS_SELECTOR, "a.ico-logout").click()

def test_invalid_credentials(driver):
    driver.get("https://demowebshop.tricentis.com/login")
    driver.find_element(By.CSS_SELECTOR,"a.ico-login").click()
    driver.find_element(By.CSS_SELECTOR,"#Email").send_keys("test@test.com")
    driver.find_element(By.CSS_SELECTOR,"#Password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR,"input[value='Log in']").click()
    title = driver.find_element(By.CSS_SELECTOR, "a.ico-logout").text
    assert title == "Log out", "successful login"
    driver.find_element(By.CSS_SELECTOR, "a.ico-logout").click()
