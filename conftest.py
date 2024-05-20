import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope='function')
def order_page(driver):
    return OrderPage(driver)