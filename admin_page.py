# page/admin_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def open_admin_tab(self):
        # Click on the Admin tab in the menu
        admin_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']"))
        )
        admin_tab.click()

    def search_user(self, username):
        # Wait for the search input to appear
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
        )
        search_input.clear()
        search_input.send_keys(username)

        # Click the search button
        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()

    def get_search_results(self):
        # Get the rows from the result table
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-row']"))
        )
