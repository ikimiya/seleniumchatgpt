import time
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from browser_utils import create_webdriver
from auth import login
from chatting import slowsend, wait_until_response_stable
from ui_controls import close_button, handle_custom_popup, handle_javascript_alert
import argparse

def main():
    parser = argparse.ArgumentParser(description="Example script to handle extra arguments.")
    parser.add_argument('--headless', action='store_true', help='Headless Chrome No Browser Launch')
    args = parser.parse_args()
    # Run the webdriver
    browser, profile_path = create_webdriver(headless=args.headless)
    try:
        browser.get("https://chatgpt.com/")
        print(f"🌐 Current Url: {browser.current_url}")
        time.sleep(3)
        print(f"🌐 After Wait - Current Url: {browser.current_url}")
        time.sleep(1.2)
        # Check If there is a close button
        try:
            close_button(browser)
        except TimeoutException:
            print("❌ Button Not Found, Continuing Anyway")
        time.sleep(1.2)

        # Click the login button
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="login-button"]'))
        )
        time.sleep(1.5)
        login_button.click()
        time.sleep(1.25)

        login(browser)
        print()
        print("✅ Logged in successfully!")
        time.sleep(3.5)

        while True:
            user_text = input("📝 What to say?: ")
            text_input = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.ID, "prompt-textarea"))
            )

            print("📨 Sending Input to Chat...",end="")
            slowsend(text_input, user_text)

            submit_btn = browser.find_element(By.ID, "composer-submit-button")
            submit_btn.click()

            print()
            print("📤 Input Sent...")
            print("⏳ Waiting For Response...",end="")

            wait_until_response_stable(browser,
                "//div[contains(@class, 'flex-col')]/div[contains(@class, 'prose')]"
            )
            print()
            responses = browser.find_elements(By.XPATH,
                "//div[contains(@class, 'flex-col')]/div[contains(@class, 'prose')]"
            )

            print("🤖 Bot Response:\n" + "-" * 50)
            print(responses[-1].text.strip())
            print("-" * 50)

            print("✅ Bot Response Finished. 🧭 Wait a Moment ... ",end="")
            handle_javascript_alert(browser)
            handle_custom_popup(browser)
            print()

    finally:
        shutil.rmtree(profile_path, ignore_errors=True)
        browser.close()

if __name__ == "__main__":
    main()
