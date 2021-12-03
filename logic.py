import api as API
import requests
from threading import Thread

def get_users_data(apikey):
    get_user_url = "https://api.slyk.io/users/id"
    get_wallet_balance_url = "https://api.slyk.io/wallets/id/balance"
    assets = API.get_wallets_balance(apikey)
    wallets = API.get_wallets(apikey)
    wallets_ids = []
    for i in wallets['data']:
        wallets_ids.append({'id':str(i['id']), 'ownerId':i['ownerId']})
    users = API.get_users(apikey)
    wallets= wallets['data']
    
    #user_data    =  threaded_process_range(28, users_ids, get_user_url, apikey)
    wallets_data  =  threaded_process_range(len(wallets_ids), wallets_ids, apikey)
    final_data = get_final_data(wallets_data, users, assets)
    return  final_data
    
def check_key_value_in_dict_list(key, value, list):
    for i in list:
        if (key, value) in i.items():
            return True

def get_final_data(wallets, users, assets):
    final_data = []
    for wallet in wallets:
        if len(wallet['data']) < len(assets['data']):
            for i in assets['data']:
                if(not check_key_value_in_dict_list("assetCode", i['assetCode'], wallet['data'])):
                    wallet['data'].append({"assetCode": i['assetCode'],"amount": 0})

        for user in users['data']:
            if(user['id'] == wallet['ownerId']):
                final_data.append({
                    'user_data': user,
                    'wallet_data': wallet,
                })
    return final_data

def process_id(id, apikey):
    """process a single ID"""
    # fetch the data
    r = requests.get("https://api.slyk.io/wallets/"+str(id)+"/balance?apikey="+apikey)
    # parse the JSON reply
    data = r.json()
    # and update some data with PUT

    return data

def process_range(id_range,apikey, store=None):
    """process a number of ids, storing the results in a dict"""
    if store is None:
        store = []
    for id in id_range:
        store.append({'id':id['id'], 'data': process_id(id['id'], apikey)['data'], 'ownerId':id['ownerId']})
    return store


from threading import Thread

def threaded_process_range(nthreads, id_range, apikey):
    """process the id range in a specified number of threads"""
    store = []
    threads = []
    # create the threads
    for i in range(nthreads):
        ids = id_range[i::nthreads]
        t = Thread(target=process_range, args=(ids,apikey, store))
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



