import os
from dotenv import load_dotenv


if __name__ == "__main__":
   print("main!")
   load_dotenv()
   key = os.environ.get("API_KEY")
   print(key)