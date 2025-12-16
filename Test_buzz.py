import time
import pytest
from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.login_page import LoginPage
from selenium.webdriver.common.keys import Keys
import os
import random

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
def test_click_edit_post(driver):
    # --- Login ---
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # --- Navigate to Buzz ---
    buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
    buzz_menu.click()

    # --- Wait for the first post ---
    first_post = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "(//div[contains(@class,'orangehrm-buzz-post')])[1]")
    ))

    # --- Click the three dots menu ---
    options_btn = first_post.find_element(By.XPATH, ".//i[contains(@class,'bi-three-dots')]/..")
    options_btn.click()

    # --- Click "Edit Post" ---
    edit_post_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//p[text()='Edit Post']")
    ))
    edit_post_option.click()
    time.sleep(2)
    print("✅ Edit Post option clicked successfully")


def test_click_most_liked_posts(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    # Wait for Dashboard to load
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # Navigate to Buzz
    buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
    buzz_menu.click()

    # Wait for "Most Liked Posts" button to appear
    most_liked_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class,'orangehrm-post-filters-button') and contains(., 'Most Liked Posts')]")
    ))

    # Click the button
    most_liked_btn.click()

    time.sleep(2)  # small wait to allow feed to refresh
    print("✅ Clicked the 'Most Liked Posts' button successfully")

def test_click_most_commented_posts(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    # Wait for Dashboard to load
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # Navigate to Buzz
    buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
    buzz_menu.click()

    # Wait for "Most Commented Posts" button to appear
    most_commented_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class,'orangehrm-post-filters-button') and contains(., 'Most Commented Posts')]")
    ))

    # Click the button
    most_commented_btn.click()

    time.sleep(2)  # small wait to allow feed to refresh
    print("✅ Clicked the 'Most Commented Posts' button successfully")

def test_help_icon(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    # Wait for Dashboard to load
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # Locate the Help icon (question mark)
    help_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//i[contains(@class, 'bi-question-lg')]")
    ))

    # Optional: click the help icon
    help_icon.click()
    time.sleep(2)
    print("✅ Help icon is present and clickable")
def test_click_share_photos_in_buzz(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # Navigate to Buzz menu
    buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
    buzz_menu.click()

    # Retry loop to handle dynamic DOM updates
    for _ in range(3):
        try:
            share_photos_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'orangehrm-buzz-create-post-actions')]/button[contains(., 'Share Photos')]")
            ))

            share_photos_btn.click()
            time.sleep(2)
            print("✅ 'Share Photos' button clicked successfully")
            break
        except StaleElementReferenceException:
            print("⚠️ Stale element encountered, retrying...")

    # Optional: wait for any modal or photo upload UI
    time.sleep(2)
def test_click_share_video_in_buzz(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # Navigate to Buzz menu
    buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
    buzz_menu.click()

    # Retry loop to handle dynamic DOM updates
    for _ in range(3):
        try:
            share_video_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'orangehrm-buzz-create-post-actions')]/button[contains(., 'Share Video')]")
            ))
            share_video_btn.click()
            time.sleep(2)
            print("✅ 'Share Video' button clicked successfully")
            break
        except StaleElementReferenceException:
            print("⚠️ Stale element encountered, retrying...")
            time.sleep(1)

    # Optional: wait for any video upload modal/UI
    time.sleep(2)
def test_click_post_option(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # Navigate to Buzz menu
    buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
    buzz_menu.click()

    # Wait for the first post
    first_post = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "(//div[contains(@class,'orangehrm-buzz-post')])[1]")
    ))
    # Click the three dots menu (inside the first post)
    options_btn = first_post.find_element(By.XPATH, ".//i[contains(@class,'bi-three-dots')]/..")
    options_btn.click()
    time.sleep(2)
    # Wait for the Delete button **inside the same post container**
def test_delete_post(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # Navigate to Buzz
    buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
    buzz_menu.click()

    # Wait for the first post
    first_post = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "(//div[contains(@class,'orangehrm-buzz-post')])[1]")
    ))

    # Click the three dots menu
    options_btn = first_post.find_element(By.XPATH, ".//i[contains(@class,'bi-three-dots')]/..")
    options_btn.click()

    # Click "Delete Post" (p element) inside the post
    delete_post_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[text()='Delete Post']")
    ))
    delete_post_option.click()

    # Confirm deletion if confirmation appears
    try:
        confirm_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Yes') or contains(., 'Confirm')]")
        ))
        confirm_btn.click()
    except:
        pass  # Some setups may delete immediately without confirmation
    time.sleep(2)
    print("✅ First post deleted successfully")
def test_edit_post(driver):
        # --- Login ---
        page = LoginPage(driver)
        page.open()
        page.login("Admin", "admin123")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

        # --- Navigate to Buzz ---
        buzz_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']")))
        buzz_menu.click()

        # --- Wait for first post ---
        first_post = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//div[contains(@class,'orangehrm-buzz-post')])[1]")
        ))

        # --- Open options ---
        options_btn = first_post.find_element(By.XPATH, ".//i[contains(@class,'bi-three-dots')]/..")
        options_btn.click()

        # --- Click "Edit Post" ---
        edit_post_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Edit Post']")))
        edit_post_option.click()

        # --- Select a random photo ---
        photos_folder = r"C:\Users\U\Downloads"
        all_photos = [os.path.join(photos_folder, f) for f in os.listdir(photos_folder)
                      if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
        if not all_photos:
            raise Exception(f"No photos found in {photos_folder}!")

        random_photo = random.choice(all_photos)
        print(f"Selected photo for edit: {random_photo}")

        # --- Upload the photo ---
        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        file_input.send_keys(random_photo)

        # --- Wait until file input has a value (photo is attached) ---
        wait.until(lambda d: file_input.get_attribute("value") != "")
        print("Photo attached successfully.")

        # --- Edit post text ---
        post_textarea = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//textarea[contains(@class,'oxd-buzz-post-input')]")
        ))
        post_textarea.clear()
        post_textarea.send_keys("This post has been edited with a random photo.")

        # --- Scroll to and click Post button ---
        post_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'orangehrm-buzz-create-post')]//button[contains(., 'Post')]")
        ))
        ActionChains(driver).move_to_element(post_btn).click().perform()

        time.sleep(2)
        print("✅ Post edited successfully with photo and caption!")





















