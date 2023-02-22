import pytest
from selenium import webdriver



@pytest.fixture
def driver():
    browser_driver = webdriver.Chrome(executable_path='chromedriver')
    option_browser_driver = webdriver.ChromeOptions()
    url = 'https://ya.ru'
    browser_driver.get(url)
    yield browser_driver
    browser_driver.quit()
