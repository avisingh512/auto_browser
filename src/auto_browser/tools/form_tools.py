from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a global driver instance
driver = webdriver.Chrome()
driver.get("http://localhost:3000")  # Adjust URL to match your React app's address

def fill_field(field: str, value: str) -> str:
    """Fill a form field with the provided value."""
    try:
        # Wait for field to be present
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.presence_of_element_located((By.ID, field))
        )
        
        # Clear existing value and type new value
        element.clear()
        element.send_keys(value)
        
        # Add a small delay to make the filling visible
        time.sleep(1)
        
        return f"Successfully filled {field} with {value}"
    except Exception as e:
        return f"Error filling {field}: {str(e)}"

def submit_form() -> str:
    """Submit the form after all fields are filled."""
    try:
        # Find and click submit button
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-button"))
        )
        
        # Add a small delay before clicking
        time.sleep(1)
        submit_button.click()
        
        # Add a delay after submission to see the result
        time.sleep(2)
        
        return "Form submitted successfully"
    except Exception as e:
        return f"Error submitting form: {str(e)}"

# Add cleanup function
def cleanup():
    driver.quit()