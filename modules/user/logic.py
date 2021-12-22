import api as API
from auxiliary import check_key_value_in_dict_list, threaded_process_range

#----------------Obtaining users balance data-------------------------#

#process users and walllets data and return final data to be show in table
def get_users_balance_data(apikey):
    assets = API.get_wallets_balance(apikey)
    wallets = API.get_wallets(apikey)
    wallets_ids = []
    for i in wallets['data']:
        wallets_ids.append({'id':str(i['id']), 'ownerId':i['ownerId']})
    users = API.get_users(apikey)
    wallets= wallets['data']
    request_url = "https://api.slyk.io/wallets/id"
    wallets_data  =  threaded_process_range(len(wallets_ids), wallets_ids, apikey, request_url)
    final_data = get_final_data(wallets_data, users, assets)
    return  final_data
    

#Helper method to transform data to be show in table
def get_final_data(wallets, users, assets):
    final_data = []
    for wallet in wallets:
        if len(wallet['data']) < len(assets['data']):
            for i in assets['data']:
                if(not check_key_value_in_dict_list("assetCode", i['assetCode'], wallet['data'])):
                    wallet['data'].append({"assetCode": i['assetCode'],"amount": 0})

        for user in users['data']:
            if(user['id'] == wallet['id_data']['ownerId']):
                final_data.append({
                    'user_data': user,
                    'wallet_data': wallet,
                })
    return final_data
#-----------------------------------------------------------------------#

#----------------Obtaining current total balance-------------------------#

def get_current_total_balance_for_asset(users_data, assets):
    total_balance = {'data':[]}
    for asset in assets['data']:
        total_balance['data'].append({'assetCode':asset['assetCode'], 'amount':0})
    for user in users_data:
        for asset in total_balance['data']:
            for wallet in user['wallet_data']['data']:
                if(wallet['assetCode'] == asset['assetCode']):
                    asset['amount'] += float(wallet['amount'])
    return total_balance
