import api as API
import requests
from threading import Thread

def get_users_data(apikey):
    get_user_url = "https://api.slyk.io/users/id"
    get_wallet_balance_url = "https://api.slyk.io/wallets/id/balance"
    assets = API.get_wallets_balance(apikey)
    wallets = API.get_wallets(apikey)['data']
    users_and_wallets_ids = [{'user_id':i['ownerId'], 'wallet_id':i['id']} for i in wallets if i['ownerId'] is not None]
    #user_data    =  threaded_process_range(28, users_ids, get_user_url, apikey)
    wallets_data  =  threaded_process_range(100, users_and_wallets_ids, get_wallet_balance_url, apikey, assets)
    return  wallets_data
    
    

def process_id(url, apikey, id, assets):
    """process a single ID"""

    user_data = API.get_user_by_id(apikey, id['user_id'])
    wallet_data = API.get_wallet_balance(apikey, id['wallet_id'])
    if len(wallet_data['data']) < len(assets['data']):
        for i in assets['data']:
            if(not check_key_value_in_dict_list("assetCode", i['assetCode'], wallet_data['data'])):
                wallet_data['data'].append({"assetCode": i['assetCode'],"amount": 0})
    print(wallet_data)
    data = {
        'user_data': user_data,
        'wallet_data': wallet_data
    }
    return data
def check_key_value_in_dict_list(key, value, list):
    for i in list:
        if (key, value) in i.items():
            return True

def process_range(id_range, url, apikey, assets, store=None):
    """process a number of ids, storing the results in a dict"""
    if store is None:
        store = []
    for id in id_range:
        request_response = process_id(url, apikey, id, assets)
        if request_response is not None:
            store.append(request_response)
    return store


def threaded_process_range(nthreads, id_range, url, apikey, assets):
    """process the id range in a specified number of threads"""
    store = []
    threads = []
    # create the threads
    for i in range(nthreads):
        ids = id_range[i::nthreads]
        t = Thread(target=process_range, args=(ids, url, apikey, assets,store))
        threads.append(t)

    # start the threads
    [ t.start() for t in threads ]
    # wait for the threads to finish
    [ t.join() for t in threads ]
    return store
def get_user_by_id(api_key, user_id):
    return API.get_user_by_id(api_key, user_id)

def get_user_orders(user_id, orders):
    user_orders = []
    for order in orders['data']:
        if order['userId'] == user_id:
            user_orders.append(order)
    return user_orders

def get_user_orders_by_status(user_id, status, payment_status, orders):
    user_orders = []
    for order in orders['data']:
        if order['userId'] == user_id and order['orderStatus'] == status and order['paymentStatus'] == payment_status:
            user_orders.append(order)
    return user_orders


def get_user_balance(user_id, orders):
    user_balance = 0
    for order in orders['data']:
        if order['userId'] == user_id and order['orderStatus'] == 'fulfilled' and order['paymentStatus'] == 'fully_paid':
            user_balance += float(order['paidAmount'])
    return user_balance

def get_orders_users_ids(apikey):
    orders = API.get_orders(apikey)
    print(len(orders['data']))
    orders_users_ids = []
    for order in orders['data']:
        if order['userId'] not in orders_users_ids:
            orders_users_ids.append(order['userId'])
    return orders_users_ids

def get_wallets_balance(apikey):
    return API.get_wallets_balance(apikey)
    
#print(user_orders)
#print(len(user_orders))
#orders_completed = get_user_orders_by_status("cES5DZL3B84Qxzt010eFmkDc0pSh1imI", "c119ff42-2bb7-4099-9187-5b99faa801a4", 'fulfilled', 'fully_paid')
#print(orders_completed)



