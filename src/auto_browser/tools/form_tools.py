from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
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
        element = wait.until(
            EC.element_to_be_clickable((By.ID, field))
        )
        
        # Get the element type
        element_type = element.get_attribute('type')

        # Handle different input types
        if element_type == 'select-one' or element.tag_name == 'select':
            return handle_select(element, value)
        elif element_type == 'select-multiple':
            return handle_multiselect(element, value)
        elif element_type == 'checkbox':
            return handle_checkbox(element, value)
        elif element_type == 'radio':
            return handle_radio(field, value)
        elif element_type == 'date':
            return handle_date(element, value)
        elif element_type == 'time':
            return handle_time(element, value)
        elif element_type == 'datetime-local':
            return handle_datetime(element, value)
        elif element_type == 'month':
            return handle_month(element, value)
        elif element_type == 'week':
            return handle_week(element, value)
        elif element_type == 'color':
            return handle_color(element, value)
        elif element_type == 'range':
            return handle_range(element, value)
        elif element.tag_name == 'textarea':
            return handle_textarea(element, value)
        else:
            # Handle regular input fields
            return handle_text_input(element, value)
        
        # Add a small delay to make the filling visible
        time.sleep(1)
        
        return f"Successfully filled {field} with {value}"
    except Exception as e:
        return f"Error filling {field}: {str(e)}"
    

def handle_select(self, element, value):
    """Handle dropdown select elements"""
    try:
        select = Select(element)
        select.select_by_visible_text(value)
        time.sleep(0.5)  # Small delay for visual feedback
        return f"Selected {value} from dropdown"
    except Exception as e:
        return f"Error handling select: {str(e)}"

def handle_multiselect(self, element, values):
    """Handle multi-select elements"""
    try:
        select = Select(element)
        if isinstance(values, str):
            values = values.split(',')
        for value in values:
            select.select_by_visible_text(value.strip())
        time.sleep(0.5)
        return f"Selected multiple values: {values}"
    except Exception as e:
        return f"Error handling multiselect: {str(e)}"

def handle_checkbox(self, element, value):
    """Handle checkbox elements"""
    try:
        current_state = element.is_selected()
        desired_state = str(value).lower() in ['true', '1', 'yes', 'on']
        if current_state != desired_state:
            element.click()
        time.sleep(0.5)
        return f"Checkbox set to {desired_state}"
    except Exception as e:
        return f"Error handling checkbox: {str(e)}"

def handle_radio(self, name, value):
    """Handle radio button elements"""
    try:
        radio = self.driver.find_element(By.CSS_SELECTOR, f"input[type='radio'][value='{value}']")
        radio.click()
        time.sleep(0.5)
        return f"Selected radio option: {value}"
    except Exception as e:
        return f"Error handling radio: {str(e)}"


def handle_date(self, element, value):
    """Handle date input elements"""
    try:
        element.clear()
        element.send_keys(value)
        time.sleep(0.5)
        return f"Set date to {value}"
    except Exception as e:
        return f"Error handling date: {str(e)}"

def handle_time(self, element, value):
    """Handle time input elements"""
    try:
        element.clear()
        element.send_keys(value)
        time.sleep(0.5)
        return f"Set time to {value}"
    except Exception as e:
        return f"Error handling time: {str(e)}"

def handle_datetime(self, element, value):
    """Handle datetime-local input elements"""
    try:
        element.clear()
        element.send_keys(value)
        time.sleep(0.5)
        return f"Set datetime to {value}"
    except Exception as e:
        return f"Error handling datetime: {str(e)}"

def handle_month(self, element, value):
    """Handle month input elements"""
    try:
        element.clear()
        element.send_keys(value)
        time.sleep(0.5)
        return f"Set month to {value}"
    except Exception as e:
        return f"Error handling month: {str(e)}"

def handle_week(self, element, value):
    """Handle week input elements"""
    try:
        element.clear()
        element.send_keys(value)
        time.sleep(0.5)
        return f"Set week to {value}"
    except Exception as e:
        return f"Error handling week: {str(e)}"

def handle_color(self, element, value):
    """Handle color input elements"""
    try:
        if not value.startswith('#'):
            value = f"#{value}"
        element.send_keys(value)
        time.sleep(0.5)
        return f"Set color to {value}"
    except Exception as e:
        return f"Error handling color: {str(e)}"

def handle_range(self, element, value):
    """Handle range input elements"""
    try:
        current_value = int(element.get_attribute('value'))
        target_value = int(value)
        
        # Calculate the number of arrow key presses needed
        steps = target_value - current_value
        
        # Use arrow keys to change value
        key = Keys.ARROW_RIGHT if steps > 0 else Keys.ARROW_LEFT
        for _ in range(abs(steps)):
            element.send_keys(key)
            time.sleep(0.1)
        
        return f"Set range to {value}"
    except Exception as e:
        return f"Error handling range: {str(e)}"

def handle_textarea(self, element, value):
    """Handle textarea elements"""
    try:
        element.clear()
        element.send_keys(value)
        time.sleep(0.5)
        return f"Set textarea content"
    except Exception as e:
        return f"Error handling textarea: {str(e)}"

def handle_text_input(element, value):
    """Handle regular text input elements"""
    try:
        element.clear()
        element.send_keys(value)
        time.sleep(0.5)
        return f"Set input value to {value}"
    except Exception as e:
        return f"Error handling text input: {str(e)}"


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