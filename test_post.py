import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()

    page.login("Admin", "admin123")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    assert "dashboard" in driver.current_url.lower()

def test_click_buzz_menu(driver):
    page = LoginPage(driver)
    page.open()

    page.login("Admin", "admin123")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//h6[text()='Dashboard']")
    ))
    buzz_menu = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Buzz']")
    ))
    buzz_menu.click()
    buzz_textarea = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//textarea[contains(@placeholder, \"What's on your mind\")]")
    ))
    assert buzz_textarea.is_displayed(), "❌ Buzz page did not load"
    time.sleep(1)

def test_buzz_post():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    username_input.send_keys("Admin")
    password_input.send_keys("admin123")
    login_button.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
    buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
    buzz_menu.click()
    buzz_textarea = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//textarea[contains(@placeholder, \"What's on your mind\")]")
    ))
    post_text = "Hello, this is a test post!"
    buzz_textarea.send_keys(post_text)
    post_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    post_button.click()

    success_toast = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@id,'oxd-toaster_1')]//p[contains(., 'Successfully Saved')]")
    ))
    assert "Successfully Saved" in success_toast.text, "❌ Success toast not displayed!"
    time.sleep(2)
    driver.quit()
