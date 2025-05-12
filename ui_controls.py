from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def handle_javascript_alert(driver):
    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"Alert detected: {alert.text}")
        alert.accept()
        return True
    except TimeoutException:
        return False

def handle_custom_popup(driver):
    try:
        popup = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Stay logged out')]"))
        )
        ok_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Okay')]")
        ok_button.click()
        return True
    except (NoSuchElementException, TimeoutException):
        return False

def close_button(browser):
    x_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="close-button"]'))
    )
    x_button.click()
    print("🖱️ X Popup Clicked!")
