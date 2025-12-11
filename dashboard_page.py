# page/dashboard_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_dashboard(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )

    def search_product(self, product_name):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
        )
        search_input.clear()
        search_input.send_keys(product_name)
        search_input.submit()  # or click the search button if needed

    def get_search_results(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'search-result-item')]"))
        )
