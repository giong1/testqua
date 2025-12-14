import time
import pytest
from selenium import webdriver
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

def test_buzz_post_success_toast():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait = WebDriverWait(driver, 10)

    # --- Step 1: Login ---
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_input.send_keys("Admin")
    password_input.send_keys("admin123")
    login_button.click()

    # Wait for Dashboard to load
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # --- Step 2: Navigate to Buzz ---
    buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
    buzz_menu.click()

    # Wait for Buzz page to load
    buzz_textarea = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//textarea[contains(@placeholder, \"What's on your mind\")]")
    ))

    # --- Step 3: Type a post ---
    post_text = "Hello, this is a test post!"
    buzz_textarea.send_keys(post_text)

    post_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    post_button.click()
    time.sleep(2)


    success_toast = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@id,'oxd-toaster_1')]//p[contains(., 'Successfully Saved')]")
    ))

    # Assert the toast message
    assert "Successfully Saved" in success_toast.text, "❌ Success toast not displayed!"



    driver.quit()
