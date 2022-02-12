from http.client import error
import urllib.request
import json
from urllib.request import  Request
from urllib.error import HTTPError
 
#return a list of all orders from the slyk
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

#return a list of all users registered in the slyk
def get_users(apikey, url="https://api.slyk.io/users?page[size]=100&sorted=createdAt"):
    return_data = {}
    try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
            data = urllib.request.urlopen(req, timeout = 100)
            json_data = json.loads(data.read())
            return_data = json_data
            total_rows = json_data['total']
    except error as e:
            print(e)
    
    except HTTPError as e:
            print(e)
        
        
    for i in range(int(total_rows/100)):
        
        try:
            req = Request(url+"&page[number]="+str(i+2), headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
            data = urllib.request.urlopen(req, timeout = 100)
            json_data = json.loads(data.read())
            return_data['data'].extend(json_data['data'])
            print(url+"&page[size]="+str(i+2))
            print(len(return_data['data']))
            
        except error as e:
            print(e)

        except HTTPError as e:
            print(e)
    return return_data

#return specific user data with a given id
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

#return a list of all wallets registered in the slyk
def get_wallets(apikey, url="https://api.slyk.io/wallets?page[size]=100&sorted=createdAt"):
    return_data = {}
    try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
            data = urllib.request.urlopen(req, timeout = 100)
            json_data = json.loads(data.read())
            return_data = json_data
            total_rows = json_data['total']
    except error as e:
            print(e)
    
    except HTTPError as e:
            print(e)
        
        
    for i in range(int(total_rows/100)):
        
        try:
            req = Request(url+"&page[number]="+str(i+2), headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
            data = urllib.request.urlopen(req, timeout = 100)
            json_data = json.loads(data.read())
            return_data['data'].extend(json_data['data'])
            print(url+"&page[size]="+str(i+2))
            print(len(return_data['data']))
            
        except error as e:
            print(e)

        except HTTPError as e:
            print(e)
    return return_data

#return a list of all wallets for an indicated page
def get_wallets_by_page(apikey, url="https://api.slyk.io/wallets?page[size]=100&sorted=createdAt"):
    return_data = {}
    try:
            req = Request(url+"page[size]=1", headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
            data = urllib.request.urlopen(req, timeout = 100)
            json_data = json.loads(data.read())
            return_data = json_data
            total_rows = json_data['total']
    except error as e:
            print(e)
    
    except HTTPError as e:
            print(e)
        

    return return_data


#return total balance of all wallets of the slyk for each existing asset       
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

#return balance of specific wallet from the slyk for each existing asset given the wallet id
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
        print(e)
        return None