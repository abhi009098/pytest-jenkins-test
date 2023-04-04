import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://demowebshop.tricentis.com")
    login = driver.find_element(By.XPATH, "//a[contains(text(),'Log in')]")
    assert login.is_displayed()
    login.click()
    email = driver.find_element(By.ID, "Email")
    email.clear()
    email.send_keys("pythontesting@gmail.com")
    password = driver.find_element(By.ID, "Password")
    password.clear()
    password.send_keys("pythontesting@123")
    login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
    assert login_button.is_displayed()
    login_button.click()
    time.sleep(3)
    logout = driver.find_element(By.XPATH, "//a[contains(text(),'Log out')]").text
    assert logout == "Log out"
    print(logout)
    driver.find_element(By.LINK_TEXT, "Log out").click()

def test_logohomepage(driver):
    driver.get("https://demowebshop.tricentis.com")
    logohomepage = driver.find_element(By.XPATH, "//a[contains(text(),'Log in')]")
    assert logohomepage.is_displayed()
    logohomepage.click()
    email = driver.find_element(By.ID, "Email")
    email.clear()
    email.send_keys("pythontesting@gmail.com")
    password = driver.find_element(By.ID, "Password")
    password.clear()
    password.send_keys("pythontesting@123")
    login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
    assert login_button.is_displayed()
    login_button.click()
    time.sleep(3)
    logout = driver.find_element(By.XPATH, "//a[contains(text(),'Log out')]").text
    assert logout == "Log out"
    LOGO = driver.find_element(By.CSS_SELECTOR, "img[alt='Tricentis Demo Web Shop']")
    assert LOGO.is_displayed()


