import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def login_to_hcm(url, email, password):
    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-notifications")

    # Set up the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the login page
        driver.get(url)  # **REPLACE THIS URL WITH YOUR HCM LOGIN PAGE URL**
        time.sleep(7)

        # Wait for the email field and enter the email
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))  
        )
        email_field.clear()
        email_field.send_keys(email)  # **REPLACE THIS WITH YOUR EMAIL**

        # Wait for the password field and enter the password
        password_field = driver.find_element(By.NAME, "password")  
        password_field.clear()
        password_field.send_keys(password)  # **REPLACE THIS WITH YOUR PASSWORD**

        # Find and click the login button
        login_button = driver.find_element(By.CLASS_NAME, "btn-primary")  
        login_button.click()
        time.sleep(10)

        # Confirm that the dashboard is visible
        dashboard_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h4")) 
        )
        if dashboard_header.text.strip() == "Dashboard":
            print("Login successful, Dashboard is visible.")
        else:
            print("Login failed or Dashboard not visible.")

    except Exception as e:
        print(f"An error occurred: {e}")

    return driver  # Return the driver object for use in further steps

#Calling the function     #only make changes here while calling for new credentials   
driver = login_to_hcm(
    "https://demo.121erp.com/hcm/login",  # URL to your login page
    "nauman.ahmad@ptclgroup.com",         # Your email
    "Ufone@123"                           # Your password
    
) 
 #uncomment  this when running login.py only 
#if using this function in another file then write these lines there only 
