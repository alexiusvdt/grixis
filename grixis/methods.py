
# headers required by API   
#    --header 'authorization: Bearer YOUR_ACCESS_TOKEN' \
#    --header 'Content-Length: 0'

# importing the requests library
import requests

def get(key, loc, **etc):
    # api-endpoint
    URL = f"https://streetviewpublish.googleapis.com/v1/photo:startUpload?key={key}"

    # location given here
    location = "grixis university"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'address':location}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()


    # extracting latitude, longitude and formatted address
    # of the first matching location
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']

    # printing the output
    print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
        %(latitude, longitude,formatted_address))

def post(key, loc, **etc):
    # defining the api-endpoint
    API_ENDPOINT = f"https://streetviewpublish.googleapis.com/v1/photo:startUpload?key={key}"    

    # your source code here
    source_code = '''
    print("Hello, world!")
    a = 1
    b = 2
    print(a + b)
    '''
    
    # data to be sent to api
    data = {'api_dev_key': API_KEY,
            'api_option': 'paste',
            'api_paste_code': source_code,
            'api_paste_format': 'python'}
    
    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=data)
    
    # extracting response text
    response = r.text
    print("The response:%s" % response)