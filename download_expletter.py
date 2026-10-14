import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
                                                                #This code is not functional

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start browser maximized
chrome_options.add_argument("--disable-notifications")


# Set up the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the login page
    driver.get("https://demo.121erp.com/hcm/login")
    time.sleep(10)

    # Wait for the email field and enter the email
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))  # Adjust if necessary
    )
    email_field.clear()
    email_field.send_keys("Nauman.ahmad@ptclgroup.com")  # **CHANGE THIS TO YOUR ACTUAL EMAIL**

    # Wait for the password field and enter the password
    password_field = driver.find_element(By.NAME, "password")  # Adjust if necessary
    password_field.clear()
    password_field.send_keys("Ufone@123")  # **CHANGE THIS TO YOUR ACTUAL PASSWORD**

    # Find and click the login button
    login_button = driver.find_element(By.CLASS_NAME, "btn-primary")  # Adjust if necessary
    login_button.click()

    # Confirm that the dashboard is the correct one
    dashboard_header = driver.find_element(By.TAG_NAME, "h4")
    if dashboard_header.text.strip() == "Dashboard":
        print("Login successful, Dashboard is visible.")
    
    # ______________________________________________________________________

    ## OPEN EMPLOYEE PROFILE TAB
    # Wait for the User Management tab to appear and click it
    user_management_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='User Management']"))
    )
    user_management_tab.click()
    print("User Management tab clicked successfully!")

    # Wait for the Employee Profile link to be clickable and click it
    employee_profile_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Employee Profile']"))
    )
    employee_profile_link.click()
    print("Employee Profile link clicked successfully!")

    # Wait for the header "Employee Profile" to appear on the page
    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h4[normalize-space(text())='Employee Profile']"))
    )
    print("Employee Profile page opened!")

    # Add a delay to keep the page open for 10 seconds to observe
    time.sleep(10)

    # _____________________________________________________________________
    # Verify clicking on employee id opens Manage employee page
      # Wait for the button to be clickable
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-outline-primary' and contains(text(), '#EMP0000072')]")))

    # Click the button
    button.click()
    print(" Employee id Button clicked successfully.")
    time.sleep(5)
    #________________________________________________________________________
    #VERIFY DOWNLOADING EXPERIENCE LETTER FUNCTIONALITY 

    #Wait for the "Experience Certificate" dropdown to be clickable
    experience_certificate_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Experience Certificate')]/.."))
    )

    # Click on the dropdown to open it
    experience_certificate_button.click()
    time.sleep(5)
    print("Experience Certificate dropdown clicked successfully!")

     # Wait for the PDF option (identified by the 'ti ti-download' class) to be clickable
    pdf_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn-icon dropdown-item']/i[contains(@class, 'ti-download')]"))
    )

    # Click the PDF option
    pdf_option.click()
    print("PDF option clicked successfully!")
    time.sleep(15)





except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()




