import requests
import asyncio
import time

async def upload(api_key, access_token):
    """
    construct params before passing request to endpoint
    creating a photo requires 3 separate calls:
    1) request url, returning an upload URL
    2) use upload url returned in 1 to upload photo bytes
    3) after photo uploaded, upload metadata
    """
    url = await get_upload_url(access_token, api_key)
    await upload_photo_bytes(access_token, url, filepath)
    await upload_metadata()

async def get_upload_url(access_token, api_key):
    """sets headers & params, returns the upload url"""
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Length': '0',
    }
    params = {'key': api_key}
    try:
        upload_url = requests.post('https://streetviewpublish.googleapis.com/v1/photo:startUpload', params=params, headers=headers)
        return upload_url
    except:
        raise Exception("get upload URL FAILED")
    
async def upload_photo_bytes(access_token, upload_url, filepath):
    """take upload url & send the photo bytes"""

    headers = {'Authorization': f'Bearer {access_token}',}
    try:
        with open(filepath, 'rb') as f:
            data = f.read()

        response = requests.post('http://UPLOAD_URL/PATH_TO_FILE', headers=headers, data=data)
    except:
        raise Exception("photobyte upload FAILED")


async def upload_metadata(access_token, api_key, upload_url):
    """slap that metadata up there"""
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }

    params = {'key': api_key}

    data = {"uploadReference":
                {
                "uploadUrl": upload_url
                },
                "pose":
                {
                    "heading": 105.0,
                    "latLngPair":
                    {
                    "latitude": 46.7512623,
                    "longitude": -121.9376983
                    }
                },
                "captureTime":
                {
                "seconds": 1483202694
                },
            }
    try:
        metadata_response = requests.post('https://streetviewpublish.googleapis.com/v1/photo', params=params, headers=headers, data=data)
    
    except:
        raise Exception("photobyte upload FAILED")
