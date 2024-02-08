import os
from dotenv import load_dotenv
import requests

def main():
    print("main!")
    #photos need metadata described in photo sphere xmp metadata to be published (https://developers.google.com/streetview/spherical-metadata)
    # metadata xmp example here: https://developers.google.com/streetview/spherical-metadata
   



if __name__ == "__main__":
   load_dotenv()
   api_key = os.environ.get("API_KEY")
   access_token = os.environ.get("ACCESS_TOKEN")
#    print(key)
   main()