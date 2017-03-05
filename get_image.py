import requests
import requests.auth
import json
from KEYS_TOKENS import *


client_auth = requests.auth.HTTPBasicAuth(USER_ID, USER_SECERT_ID)
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUserName"}

def get_random_url():
    print('getting random url')
    response = requests.get(
            "https://www.reddit.com/r/TinyTrumps/random",
            auth=client_auth,
            headers=headers
            )
    return response

def get_random_image_jpg(url):
    print('getting random image')
    if url.status_code == 200:
        image_url = url.url[:-1] + ".json"
        image_response = requests.get(image_url, auth=client_auth, headers=headers)
        image_jpg = image_response.json()[0]['data']['children'][0]['data']['preview']['images'][0]['source']['url']
        return image_jpg
