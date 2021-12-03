%%timeit -r 1
import requests
from requests_futures.sessions import FuturesSession
from concurrent.futures import ProcessPoolExecutor
from http.client import error
import urllib.request
import json
from urllib.request import  Request
from urllib.error import HTTPError

def fetch(session, url):
    with session.get(url) as response:
            print(response.json())
            return response.json()

apikey = "cES5DZL3B84Qxzt010eFmkDc0pSh1imI"

try:
            req = Request("https://api.slyk.io/wallets", headers={'User-Agent': 'Mozilla/5.0', 'apiKey': apikey})
            data = urllib.request.urlopen(req, timeout = 100)
            json_data = json.loads(data.read())
            wallets = json_data
except error as e:
            print(e)
    
except HTTPError as e:
            print(e)
        

wallets_urls = []
balance = []
for i in wallets['data']:
        wallets_urls.append("https://api.slyk.io/wallets/"+str(i['id'])+"/balance?apikey=cES5DZL3B84Qxzt010eFmkDc0pSh1imI")

        


with FuturesSession(executor=ProcessPoolExecutor(max_workers=len(wallets_urls))) as session:
                    futures = [session.get(url) for url in wallets_urls]
                    for future in futures:
                        balance.append(future.result())
print(balance[0].)
print(len(balance))