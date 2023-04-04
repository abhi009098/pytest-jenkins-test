import pytest


def test_setup():
    global driver
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.selenium_manager import SeleniumManager
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)


def test_login():
    driver.get('https://demowebshop.tricentis.com')  # get command opening the application Url
    title = driver.title  # captures the title of current page
    assert title == "Demo Web Shop"
    url = driver.current_url  # captures the current Url of page-https://letcode.in/test-practice
    assert url == "https://demowebshop.tricentis.com/"
    # print(driver.page_source)  # captures the source Code of  page-very big codes will come


def test_teardown():
    # driver.close()
    print("test is completed")
