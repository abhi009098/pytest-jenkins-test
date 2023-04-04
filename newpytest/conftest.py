import pytest


@pytest.fixture()
def driver():
    global driver
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    driver.find_element(By.CSS_SELECTOR,"")


# @pytest.fixture(autouse=True)
# def driver():
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()


# def test_example(browser):
#     browser.get("https://www.example.com")
#     assert "Example Domain" in browser.title
# scope="session",
#scope="module"
# @pytest.fixture(scope="session",autouse=True)
# def driver():
#     print("open browser")
#     print("login")
#     yield
#     print("logout")

# @pytest.fixture(autouse=True)
# def addno():
#     num = 100
#     return num



