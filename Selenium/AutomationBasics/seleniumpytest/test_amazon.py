import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.amazon.in/')
    yield driver
    driver.quit()

def test_open_amazon(driver):
    driver.find_element(By.CLASS_NAME, "a-button-text").click()
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    assert "Amazon" in driver.title, 'Amazon not found in title'
    print("\nOpened Amazon Homepage. Title verified.")

def test_search_product(driver):
    wait = WebDriverWait(driver,10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()
    # assert "wireless" in driver.current_url
    assert driver.current_url.__contains__('wireless'), 'Search results page did not loaded'
    assert driver.title.__contains__('wireless'), 'Search results page did not loaded'
    print("\nSearch results page loaded successfully.")


def test_find_elements_amazon(driver):
    wait = WebDriverWait(driver,100)

    # Single product title
    first_product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a h2 span")))
    print("\nFirst Product: ", first_product.text)

    product_titles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a h2 span")))
    print(f"\nFound {len(product_titles)} product titles on page one.\n")

    for i,title in enumerate(product_titles[:5], start=1):
        print(f"{i}. {title.text}")

    assert len(product_titles) > 0, "No products found on Amazon search results!"

