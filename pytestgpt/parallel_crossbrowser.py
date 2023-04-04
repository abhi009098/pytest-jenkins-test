# import pytest
# from selenium import webdriver
#
# @pytest.fixture
# def browser(request):
#     driver = request.param()
#     yield driver
#     driver.quit()
#
# @pytest.mark.parametrize('browser', [webdriver.Chrome, webdriver.Edge,webdriver.Firefox], indirect=True)
# def test_example(browser):
#     browser.get('https://demowebshop.tricentis.com')
#     assert browser.title == 'Demo Web Shop'


import pytest
from selenium import webdriver

"""It creates a dictionary of browser names and webdriver classes,then uses a fixture to parameterize the test
 with the browser keys. The fixture also takes care of initializing  and quitting the driver for each test"""

browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox,
    'edge': webdriver.Edge
}

"""This fixture is used to instantiate the browser objects of different browsers. 
It takes the values from the "params" argument from the "browsers" dictionary and yields the driver object.
 After the test execution is done, the driver object is then exited."""
@pytest.fixture(params=browsers.keys())
def browser(request):
    driver = browsers[request.param]()
    yield driver
    driver.quit()

def test_example2(browser):
    browser.get('https://demowebshop.tricentis.com')
    assert browser.title == 'Demo Web Shop'
    print(browser.title)

def test_example3(browser):
    browser.get('https://demowebshop.tricentis.com')
    assert browser.current_url == 'https://demowebshop.tricentis.com/'
    print(browser.current_url)

