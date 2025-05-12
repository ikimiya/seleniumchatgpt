
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Send with delay and pauses to simulate real human
def slowsend(letters, text, min_delay=0.05, max_delay=0.15, occasional_pause_chance=0.1):
    for i, char in enumerate(text):
        letters.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))
        if random.random() < occasional_pause_chance and i > 5:
            time.sleep(random.uniform(0.2, 0.4))


# Response control to check if chatbot is still updating or not
def wait_until_response_stable(browser, xpath, min_stable_time=5, timeout=90, post_stable_buffer=2):
    end_time = time.time() + timeout
    previous_text = ""
    stable_start = None

    while time.time() < end_time:
        elements = browser.find_elements(By.XPATH, xpath)
        if not elements:
            time.sleep(0.22)
            continue

        current_text = elements[-1].text.strip()
        if current_text != previous_text:
            previous_text = current_text
            stable_start = time.time()
        elif stable_start and (time.time() - stable_start >= min_stable_time):
            time.sleep(post_stable_buffer)
            latest_text = elements[-1].text.strip()
            if latest_text == previous_text:
                return latest_text
            else:
                previous_text = latest_text
                stable_start = time.time()

        time.sleep(0.2)

    raise TimeoutError("Bot response did not finish in time.")
