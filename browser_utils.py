import time
import random
import shutil
from tempfile import mkdtemp
from fake_useragent import UserAgent
import undetected_chromedriver as uc
from selenium import webdriver

def create_webdriver(headless = False):
    # Temporary user profile path
    user_data_dir = mkdtemp()

    # Random user agent
    ua = UserAgent()
    user_agent = ua.random

    # Set Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument(f"--user-agent={user_agent}")
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--disable-dev-shm-usage')

    # To make it browserless remove the cmd based
    # --headless for headless else nothing
    if(headless):
        options.add_argument('--headless')

    # Launch browser settings
    driver = uc.Chrome(options=options, enable_cdp_events=True)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver, user_data_dir
