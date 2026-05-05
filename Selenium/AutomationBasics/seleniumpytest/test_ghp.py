#Google_HomePage


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pytest_check as check



@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_ghpload(driver):
    page_title = driver.title
    assert page_title == 'Google', 'Google Home Page Not Loaded'


def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT, 'Images').click()
    pagetitle = driver.title
    assert pagetitle == 'Google Images', 'Images Page Not Loaded'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT, 'Business').click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.title_contains('Business'))
    #---Hard Assersion---
    # assert 'Business' in driver.title, 'Business Page Not Loaded - Title Check'
    # assert 'business' in driver.current_url, 'Business Page Not Loaded - URL Check'
    #--Soft Assersion---
    check.is_in( 'Business',driver.title,'Business Page Not Loaded - Title Check')
    check.is_in('business', driver.current_url, 'Business Page Not Loaded - URL Check')


