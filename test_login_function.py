import time
from playwright.sync_api import sync_playwright

def test_login_to_hdss(url, email, password):
    
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)   # headless=True runs in background
    page = browser.new_page()
    
    try:
        # Open the login page
        page.goto(url)
        time.sleep(2)

        # Enter credentials
        page.fill("input[name=email]", email)
        page.fill("input[name=password]", password)

        # Click login
        page.click("button[type='submit']")
        page.wait_for_load_state("networkidle")
        time.sleep(2)

        # Confirm login by checking dashboard element
        if page.is_visible("text=Dashboard"):
            print(" Login successful, Dashboard is visible.")
        else:
            print(" Login failed or Dashboard not visible.")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Return page & browser for further use
    return browser, page

#browser, page = test_login_to_hdss(
 #   "http://172.16.35.28:4242/login", 
  #  "imran", 
   # "Test@123"
#)

