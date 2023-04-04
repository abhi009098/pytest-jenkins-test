import pytest


@pytest.fixture()
def test_setup():
    global driver
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    # driver.close()
    print("test is completed")


#@pytest.mark.usefixtures("test_setup")
def test_login(test_setup):
    driver.get('https://demowebshop.tricentis.com')  # get command opening the application Url
    title = driver.title  # captures the title of current page
    assert title == "Demo Web Shop"
    url = driver.current_url  # captures the current Url of page-https://letcode.in/test-practice
    assert url == "https://demowebshop.tricentis.com/"
    # print(driver.page_source)  # captures the source Code of  page-very big codes will come

#@pytest.mark.usefixtures("test_setup")
def test_twitter(test_setup):
    driver.get("https://twitter.com/")
    assert driver.title == "Twitter" or 'Explore / Twitter'
