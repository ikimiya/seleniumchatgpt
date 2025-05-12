import os
from dotenv import load_dotenv

load_dotenv(override=True)

username = os.getenv("USER")
password = os.getenv("CHAT")
