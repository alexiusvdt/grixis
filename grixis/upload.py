import requests
import asyncio
import time

# DRY refactor suggestion: dedicated header creation

async def upload(api_key, access_token, filepath, payload):
    """Performs 3 async calls in sequence to upload the 360 file with metadata"""
    data = payload
    url = await get_upload_url(access_token, api_key)
    await upload_photobytes(access_token, url, filepath)
    await upload_metadata(access_token, api_key, url, data)

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
        raise Exception("1 - get upload URL FAILED")
    
async def upload_photobytes(access_token, upload_url, filepath):
    """takes a file path, constructs headers, and POSTS to url"""

    headers = {'Authorization': f'Bearer {access_token}',}
    try:
        with open(filepath, 'rb') as f:
            data = f.read()

        response = requests.post(f'http://{upload_url}/{filepath}', headers=headers, data=data)
    except:
        raise Exception("2 - photobyte upload FAILED")


async def upload_metadata(access_token, api_key, upload_url, data):
    """constructs header and params, sets data dict to POST, """
    
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
        raise Exception("3 - metadata upload FAILED")
