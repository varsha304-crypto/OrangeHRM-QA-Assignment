# OrangeHRM QA Automation Assignment

## Project Overview

This project is a QA Automation assignment developed using **Python**, **Selenium WebDriver**, and the **Page Object Model (POM)** framework.

The automation script performs the following tasks:

- Login to the OrangeHRM application
- Navigate to the PIM module
- Add multiple employees
- Verify employees in the Employee List
- Logout from the application

---

## Website

https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

**Username:** Admin

**Password:** admin123

---

## Technologies Used

- Python 3.x
- Selenium WebDriver
- Chrome Browser
- Visual Studio Code

---

## Project Structure

```
OrangeHRM_Automation
│
├── pages
│   ├── login_page.py
│   └── pim_page.py
│
├── tests
│   └── test.py
│
├── utils
│   └── driver.py
│
├── requirements.txt
└── README.md
```

---

## Features

- Login Automation
- Navigate to PIM Module
- Add Employees
- Verify Employee Records
- Logout Automation

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/varsha304-crypto/OrangeHRM-QA-Assignment.git
```

### 2. Open the Project

Open the project folder in Visual Studio Code.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Automation Script

```bash
python -m tests.test
```

---

## Test Scenario

1. Launch OrangeHRM website
2. Login with valid credentials
3. Open PIM module
4. Add multiple employees
5. Verify employees in Employee List
6. Logout successfully

---

## Framework Used

This project follows the **Page Object Model (POM)** design pattern.

- **pages/** contains page classes
- **utils/** contains browser setup
- **tests/** contains the execution script

---

## Author

**Varsha Sri Lingineni**

QA Engineer Assignment – 2026