from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loading_screen import show_loading_screen

def report_accounts(username, accounts_file):
    options = Options()
    options.add_argument("--disable-notifications")  # Disable notifications

    # Read account credentials from file
    with open(accounts_file, "r") as file:
        accounts = [line.strip().split(":") for line in file if line.strip()]

    # Initialize WebDriver
    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException as e:
        print("Error: WebDriver initialization failed.")
        print(e)
        return

    # Iterate through accounts
    for account in accounts:
        if len(account) < 2:  # Ensure valid account information
            print(f"Invalid account entry: {account}")
            continue

        try:
            # Log in
            driver.get("https://www.instagram.com/accounts/login/")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
            
            username_field = driver.find_element(By.NAME, "username")
            username_field.clear()  # Clear the field before entering
            username_field.send_keys(account[0])

            password_field = driver.find_element(By.NAME, "password")
            password_field.clear()  # Clear the field before entering
            password_field.send_keys(account[1])

            # Find and click the submit button
            submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            submit_button.click()
            show_loading_screen(10)

            # Visit target user's page
            driver.get(f"https://www.instagram.com/{username}/")
            show_loading_screen(10)

            # Report user
            option_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//svg[@aria-label='Options']")))
            option_button.click()
            show_loading_screen(2)

            report_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Report']")))
            report_button.click()
            show_loading_screen(2)

            # Confirm report
            report_confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Report']")))
            report_confirm_button.click()
            show_loading_screen(2)

            # Choose reason for reporting
            spam_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='It's spam']")))
            spam_button.click()
            show_loading_screen(3)

            # Close report modal
            close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']")))
            close_button.click()
            show_loading_screen(3)

            # Log out
            logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log Out']")))
            logout_button.click()
            show_loading_screen(2)

            confirm_logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log Out']")))
            confirm_logout_button.click()
            show_loading_screen(3)

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error occurred while processing account {account[0]}: {e}")
            continue

    driver.quit()
