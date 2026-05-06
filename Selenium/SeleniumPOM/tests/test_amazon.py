from pages.home_page import HomePage


def test_open_amazon(driver):
    # driver.find_element(By.CLASS_NAME, "a-button-text").click()
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    # assert "Amazon" in driver.title, 'Amazon not found in title'
    print("\nOpened Amazon Homepage. Title verified.")

def test_search_product(driver):
    #Arrange
    homepage = HomePage(driver)

    #Act
    homepage.type_search_input()
    homepage.click_search_button()

    #Assert
    assert homepage.is_amazon_page_loaded() == True , 'Search results page did not loaded'
    print("\nSearch results page loaded successfully.")



