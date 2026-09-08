from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

    def login(self, username, password):

        self.wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        ).send_keys(username)

        self.driver.find_element(
            By.NAME,
            "password"
        ).send_keys(password)

        self.driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Dashboard']")
            )
        )

    def logout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "oxd-userdropdown-tab")
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='Logout']")
            )
        ).click()