import os
from dotenv import load_dotenv
import requests
from upload import upload

def main():
    print("main!")
    #photos need metadata described in photo sphere xmp metadata to be published (https://developers.google.com/streetview/spherical-metadata)
    # metadata xmp example here: https://developers.google.com/streetview/spherical-metadata

   # grab the filepath
   # error check files
      # check that metadata is properly formatted
      # check that all files are present
      #
   # call upload script
   # cleanup & process next/close
   upload(acc)

if __name__ == "__main__":
   load_dotenv()
   api_key = os.environ.get("API_KEY")
   access_token = os.environ.get("ACCESS_TOKEN")
#    print(key)
   main()