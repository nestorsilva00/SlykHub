from http.client import error
import urllib.request
import json
from urllib.request import  Request
from urllib.error import HTTPError
 
def get_orders(apikey, url="https://api.slyk.io/orders"):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
        data = urllib.request.urlopen(req, timeout = 100)
        json_data = json.loads(data.read())
        return json_data
    except error as e:
        print(e)
        return None
    except HTTPError as e:
        print(e)
        return None

def get_users(apikey, url="https://api.slyk.io/users"):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
        data = urllib.request.urlopen(req, timeout = 100)
        json_data = json.loads(data.read())
        return json_data
    except error as e:
        print(e)
        return None
    except HTTPError as e:
        print(e)
        return None

def get_user_by_id(api_key, user_id, url="https://api.slyk.io/users"):
    try:
        req = Request(url+"/"+user_id, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': api_key})
        data = urllib.request.urlopen(req, timeout = 100)
        json_data = json.loads(data.read())
        return json_data
    except error as e:
        print(e)
        return None
    except HTTPError as e:
        print(e)
        return None

def get_wallets(apikey, url="https://api.slyk.io/wallets"):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
        data = urllib.request.urlopen(req, timeout = 100)
        json_data = json.loads(data.read())
        return json_data
    except error as e:
        print(e)
        return None
    except HTTPError as e:
        print(e)
        return None

def custom_request(url, apikey):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
        data = urllib.request.urlopen(req, timeout = 100)
        json_data = json.loads(data.read())
        return json_data
    except error as e:
        print(e)
        return None
    except HTTPError as e:
        print(e)
        return None
       

def get_wallets_balance(apikey, url="https://api.slyk.io/wallets/balance"):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
        data = urllib.request.urlopen(req, timeout = 100)
        json_data = json.loads(data.read())
        return json_data
    except error as e:
        print(e)
        return None
    except HTTPError as e:
        print(e)
        return None

def get_wallet_balance(apikey, id):
    try:
        url="https://api.slyk.io/wallets/"+id+"/balance"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
        data = urllib.request.urlopen(req, timeout = 100)
        json_data = json.loads(data.read())
        return json_data
    except error as e:
        print(e)
        return None
    except HTTPError as e:
        print("404 en wallet balance, id:"+id)
        return None