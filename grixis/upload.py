import requests

def upload(api_key, access_token):
    """
    construct params before passing request to endpoint
    creating a photo requires 3 separate calls:
    1) request url, returning an upload URL
    2) use upload url returned in 1 to upload photo bytes
    3) after photo uploaded, upload metadata
    """    
    resp = get_upload_url()
    if resp == "<Response [200]>":
        print("yay")
    else:
        print("ohr noer")

def get_upload_url():
    """get the upload url"""

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Length': '0',
    }

    params = {
        'key': api_key,
    }

    upload_url = requests.post('https://streetviewpublish.googleapis.com/v1/photo:startUpload', params=params, headers=headers)
    return upload_url
    
def upload_photo_bytes(upload_url, filepath):
    """take upload url & send the photo bytes"""

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    with open(filepath, 'rb') as f:
        data = f.read()

    response = requests.post('http://UPLOAD_URL/PATH_TO_FILE', headers=headers, data=data)

def upload_metadata():
    """slap that metadata up there"""
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }

    params = {
        'key': api_key,
    }

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
    metadata_response = requests.post('https://streetviewpublish.googleapis.com/v1/photo', params=params, headers=headers, data=data)
