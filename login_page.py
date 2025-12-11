from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, user, pwd):
        wait = WebDriverWait(self.driver, 10)

        # Wait for username field
        wait.until(EC.visibility_of_element_located(self.username))

        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(user)

        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(pwd)

        self.driver.find_element(*self.login_button).click()
