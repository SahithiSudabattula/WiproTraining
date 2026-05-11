import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    # driver.find_element(By.CLASS_NAME, "a-button-text").click()
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    # assert "Amazon" in driver.title, 'Amazon not found in title'
    print("\nOpened Amazon Homepage. Title verified.")


@pytest.mark.parametrize(("searchproduct", "brandname", "mensize"),
[
    ("shoes", "Nike", "9")
])
def test_product_ordering(driver, searchproduct, brandname, mensize):
    # Arrange
    homepage = HomePage(driver)

    # Act
    homepage.type_search_input(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_button()

    # Assert
    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not loaded'
    print("\nSearch results page loaded successfully.")

    productlistingpage = ProductListingPage(driver)
    print(f"Applying Brand Filter - {brandname}")
    productlistingpage.select_brand_filter(brandname)

    assert productlistingpage.check_product_titles_for_brand_filters(brandname), 'Brand filter did not apply'
    print(f"Applying Size Filter for men's Shoes - {mensize}")
    productlistingpage.select_mensize_filter(mensize)

    assert productlistingpage.check_size_in_title(mensize), 'Mensize filter did not apply'



