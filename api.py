from http.client import error
import urllib.request
import json
from urllib.request import  Request
 
def get_data_from_api(url, apikey):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
        data = urllib.request.urlopen(req, timeout = 100)
        json_data = json.loads(data.read())
        print(req.headers)
        return json_data
    except error as e:
        print(e)

