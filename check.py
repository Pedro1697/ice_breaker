import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SCRAPIN_API_KEY")
print(api_key)  # mostrará sin comillas
