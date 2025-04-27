# ChatGPT Selenium

ChatGPT Selenium is a project that uses web scraping and the Selenium WebDriver to interact with ChatGPT without needing to visit the website directly, by operating in headless mode.  
This tool is unfinished and require human interaction when needed. This program focuses on web scraping and automation to retrieve and send ChatGPT responses.  
It currently requires some human interaction at the login stage and **may crash** if unexpected popups or bot detection occurs. 

---

# Info

- Access ChatGPT responses without manually opening the website
- Basic methods to avoid detection using undetected chrome and randomize user agent

---

# Prerequisites

1. Install the required libraries listed in the `chatgpt.py` script.
2. Create a `.env` file in the project directory with the following contents:
CHAT=PASS
USER=EMAIL
---

# Usage

- Run the `chatgpt.py` script after setting up the environment.
- The script will launch a headless browser session, log in automatically, and allow you to send prompts and receive responses.
- If any unexpected popups or detections occur, it will crash the program.

---

# Notes

- This tool is for educational purposes for using skills of webscraping and selenium
- **Using ChatGPT without API is against (TOS).** 
- So use at your own risk.

---