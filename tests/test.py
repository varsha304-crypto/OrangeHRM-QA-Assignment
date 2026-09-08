from utils.driver import get_driver
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
import traceback


def main():

    # Launch Browser
    driver = get_driver()

    # Create Objects
    login = LoginPage(driver)
    pim = PIMPage(driver)

    try:

        # Open OrangeHRM
        login.open()

        # Login
        login.login("Admin", "admin123")
        print("Login Successful")

        # Open PIM
        pim.open_pim()

        # Employees to Add
        employees = [
            ("Varsha", "Lingineni"),
            ("Likitha", "Lingineni"),
            ("Bhavya", "Lingineni"),
            ("Kalyani", "Lingineni")
        ]

        # Add Employees
        for first_name, last_name in employees:

            pim.add_employee(first_name, last_name)

            # Return to PIM for next employee
            pim.open_pim()

        # Verify Employees
        for first_name, last_name in employees:

            pim.verify_employee(first_name)

        # Logout
        login.logout()

        print("Logout Successful")

    except Exception:

        print("Automation Failed")
        traceback.print_exc()

    finally:

        driver.quit()


if __name__ == "__main__":
    main()