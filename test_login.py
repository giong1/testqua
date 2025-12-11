import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.login_page import LoginPage



def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()

    # Login using correct credentials
    page.login("Admin", "admin123")

    # Wait for Dashboard label to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    # Assert we are on dashboard page
    assert "dashboard" in driver.current_url.lower()


def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open()

    # Login using wrong credentials
    page.login("WrongUser", "WrongPassword")

    # Wait for error message and verify it
    error_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]"))
    )

    assert "Invalid credentials" in error_text.text
