import time
import random
import shutil
from tempfile import mkdtemp

import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os
import random

def create_webdriver():
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
    #options.add_argument("--headless")

    # Launch browser
    driver = uc.Chrome(options=options,enable_cdp_events=True)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver, user_data_dir

# Run the browser
browser, profile_path = create_webdriver()

# Load Private Loggin Info
load_dotenv(override=True)
username = os.getenv("USER")
password = os.getenv("CHAT")

def slowsend(letters, text):
    for char in text:
        letters.send_keys(char)
        time.sleep(random.uniform(0.09, 0.323))

def login(browser):

    print("Currently Logging In")
    user_login = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id=':r1:-email']"))
    )

    time.sleep(2)
    print("Sending Username")
    slowsend(user_login,username)
    time.sleep(1.2)
    continue_button = browser.find_element(By.XPATH, "//*[@id=':r1:']/div[2]/button")
    time.sleep(1.3)
    continue_button.click()
    time.sleep(1.4)

    password_login = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id=':re:-password']"))
    )
    print("Sending Password")
    time.sleep(2)
    slowsend(password_login,password)
    time.sleep(1)

    continue_button = browser.find_element(By.XPATH, "// *[ @ id = ':re:'] / div[2] / button")

    time.sleep(2)
    continue_button.click()

try:

    #chatmain = "https://chatgpt.com/"
    # Login Page must use to prevent
    link = "https://chatgpt.com/"
    auth = "https://auth.openai.com/log-in"
    browser.get(link)
    print(f"Current Url:" + str(browser.current_url))

    time.sleep(random.uniform(2.5,3.6))

    print(browser.current_url)
    print(link)

    if(link != auth):
        print("Error Login Page changed")
        #login(browser)
        browser.get(auth)
        shutil.rmtree(profile_path, ignore_errors=True)

    time.sleep(2)
    # Login to the website
    login(browser)

    # First Text To Begin
    # Possible to use this as a setup

    # Get user input
    mytext = input("What to say?: ")
    time.sleep(random.uniform(0.5, 1.5))

    text_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "prompt-textarea"))
    )

    slowsend(text_input,mytext)

    # Begin finding first button
    buttonfind = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.ID,"composer-submit-button"))
    )

    time.sleep(random.uniform(0.5, 1.5))
    buttonfind.click()
    time.sleep((5))

    first_response = True
    keepGoing = True

    while(keepGoing):
        # Get the first response and only newer response
        old_response_elements = browser.find_elements(By.XPATH,"//div[contains(@class, 'flex-col')]/div[contains(@class, 'prose')]")
        old_count = len(old_response_elements)

        #print first response once
        if(first_response):
            first_response = False
            for response in old_response_elements:
                print("Bot:", response.text)
        time.sleep(3)

        mytext = input("What to say?: ")
        text_input = browser.find_element(By.ID, "prompt-textarea")
        slowsend(text_input, mytext)
        time.sleep(random.uniform(0.5, 1.5))

        # Find the submit button and click it
        submit_button = browser.find_element(By.ID, "composer-submit-button")
        submit_button.click()

        time.sleep(5)
        # Wait response
        WebDriverWait(browser, 20).until(
            lambda b: len(b.find_elements(By.XPATH,
                                          "//div[contains(@class, 'flex-col')]/div[contains(@class, 'prose')]")) > old_count
        )

        # get the new responses
        all_response_elements = browser.find_elements(By.XPATH,"//div[contains(@class, 'flex-col')]/div[contains(@class, 'prose')]")
        new_responses = all_response_elements[old_count:]

        # Print each new full response
        for response in new_responses:
            print("Bot:", response.text)

        # Reload
        time.sleep((5))

except KeyboardInterrupt as e:
    print(f"Keyboard Exception Occured {e}")
    shutil.rmtree(profile_path, ignore_errors=True)
    browser.close()

except browser.close():
    shutil.rmtree(profile_path, ignore_errors=True)
    browser.close()
finally:
    shutil.rmtree(profile_path, ignore_errors=True)





