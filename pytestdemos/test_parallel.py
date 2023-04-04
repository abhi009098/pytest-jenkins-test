# import pytest
#
#
# def test_google():
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     driver.get("https://www.google.co.in/")
#     assert driver.title == "Google"
#
# def test_facebook():
#     # from selenium import webdriver
#     # from selenium.webdriver.common.by import By
#     # driver = webdriver.Chrome()
#     # driver.implicitly_wait(5)
#     # driver.maximize_window()
#     driver.get("https://www.facebook.com/")
#     assert driver.title  == "Facebook – log in or sign up"
#
#
# def test_instagram():
#     # # from selenium import webdriver
#     # # from selenium.webdriver.common.by import By
#     # # driver = webdriver.Chrome()
#     # # driver.implicitly_wait(5)
#     # # driver.maximize_window()
#     # # driver.get("https://www.instagram.com/")
#     # assert driver.title == "Instagram"
#     # driver.close()
#
# def test_twitter():
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     driver.get("https://twitter.com/")
#     assert driver.title == "Twitter" or 'Explore / Twitter'
#
#
# def test_telegram():
#     # from selenium import webdriver
#     # driver = webdriver.Chrome()
#     # driver.implicitly_wait(5)
#     driver.get("https://telegram.org/")
#     assert driver.title == "Telegram Messenger"
#
