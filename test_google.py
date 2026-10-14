from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
## PYTEST EXAMPLE



def test_google_search():
    # Start the browser
    driver = webdriver.Chrome()

    # Open Google
    driver.get("https://www.google.com")
    
    # Check if the title contains "Google"
    assert "Google" in driver.title, "Google homepage did not load!"
    
    # Find the search box and type the search query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    
    # Wait for search results to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
        )
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        assert len(results) > 0, "No search results were found!"
    except Exception as e:
        print(f"Error: {e}")

    # Close the browser
    driver.quit()
