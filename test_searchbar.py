import pytest
from page.login_page import LoginPage
from page.dashboard_page import DashboardPage

def test_searchbar(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.wait_for_dashboard()

    # Search for a product
    dashboard.search_product("Test Product")

    # Get search results
    results = dashboard.get_search_results()

    # Assert that at least one result is returned
    assert len(results) > 0
