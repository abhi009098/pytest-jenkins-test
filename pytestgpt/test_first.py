import time

# from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_1():
    a = 10
    b = 10
    assert a == b
def test_2():
    a = "selenium"
    b = "selenium is a great tool for automation"
    assert a in b

def test_3():
    a = "selenium"
    b = "selenium is a great tool for automation"
    assert a is b

def test_4():

    from selenium import webdriver
    from pyshadow.main import Shadow
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    time.sleep(5)
    shadow = Shadow(driver)

    # find the input element inside the shadow root
    input = shadow.find_element("#kils")
    input.send_keys("selenium")

    # click on the input element
    print(input.get_attribute("value"))
    time.sleep(5)