import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from urllib.parse import urlparse
from configurations import username, password
from chatting import slowsend

def is_different_domain(current_link, browser_url):
    domain1 = urlparse(current_link).netloc
    domain2 = urlparse(browser_url).netloc
    return domain1 != domain2

def login(browser):
    try:
        current_link = browser.current_url
        print("🔐 Attempting to log in...",end="")
        user_login = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id=':r1:-email']"))
        )
        time.sleep(1.5)
        slowsend(user_login, username)
        time.sleep(1.5)

        #Continue Button
        continue_button = browser.find_element(By.XPATH, "//*[@id=':r1:']/div[2]/button")
        time.sleep(1.3)
        continue_button.click()
        time.sleep(1.4)

        try:
            # If google account login
            if is_different_domain(current_link, browser.current_url):
                next_button = browser.find_element(By.XPATH, "//span[text()='Next']")
                next_button.click()
                time.sleep(1.5)
                password_field = browser.find_element(By.NAME,"Passwd")
                slowsend(password_field,password)
                time.sleep(1.2)
                next_button2 = browser.find_element(By.XPATH, "//span[text()='Next']")
                next_button2.click()
                time.sleep(2)
                print("Update if Login Or Not")
                return
        except Exception as e:
            print(f"Not Google Account Continue")

        password_login = WebDriverWait(browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id=':re:-password']"))
        )
        slowsend(password_login, password)
        time.sleep(3)
        browser.find_element(By.XPATH, "// *[ @ id = ':re:'] / div[2] / button").click()
        time.sleep(3)

    except Exception as e:
        print(f"Login failed: {e}")
