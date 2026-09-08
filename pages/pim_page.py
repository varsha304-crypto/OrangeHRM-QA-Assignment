from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PIMPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # -----------------------------
    # Open PIM
    # -----------------------------
    def open_pim(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='PIM']")
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='PIM']")
            )
        )

    # -----------------------------
    # Add Employee
    # -----------------------------
    def add_employee(self, first_name, last_name):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Add Employee")
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "firstName")
            )
        ).send_keys(first_name)

        self.driver.find_element(
            By.NAME,
            "lastName"
        ).send_keys(last_name)

        save = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            save
        )

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Personal Details']")
            )
        )

        print(first_name, last_name, "Added")

    # -----------------------------
    # Verify Employee
    # -----------------------------
    def verify_employee(self, first_name):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Employee List")
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
            )
        )

        search = self.driver.find_element(
            By.XPATH,
            "(//input[@placeholder='Type for hints...'])[1]"
        )

        search.clear()
        search.send_keys(first_name)

        self.driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

        time.sleep(3)

        if first_name.lower() in self.driver.page_source.lower():
            print(first_name, "Name Verified")
        else:
            print(first_name, "Not Found")

        self.driver.refresh()

        time.sleep(2)