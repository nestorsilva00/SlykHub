import requests
from threading import Thread

#Check if a key/value combination exists in a list of dictionaries
def check_key_value_in_dict_list(key, value, list):
    for i in list:
        if (key, value) in i.items():
            return True


#-----------------------------------------------------------------------------#
#------------------------Parallale multiple API calls-------------------------#

#process a single id calling the API request that corresponds to the id
def process_id(id, apikey, request_url):
    """process a single ID"""
    # fetch the data
    request_url = request_url.replace("id", id)
    r = requests.get(request_url+"/balance?apikey="+apikey)
    # parse the JSON reply
    data = r.json()


    return data

#process a range of API requests using ids
def process_range(id_range,apikey, request_url, store=None):
    """process a number of ids, storing the results in a dict"""
    if store is None:
        store = []
    for id in id_range:
        store.append({'id_data':id, 'data': process_id(id['id'], apikey, request_url)['data']})
    return store


from threading import Thread

#creating threads to process a range of ids
def threaded_process_range(nthreads, id_range, apikey, request_url):
    """process the id range in a specified number of threads"""
    store = []
    threads = []
    # create the threads
    for i in range(nthreads):
        ids = id_range[i::nthreads]
        t = Thread(target=process_range, args=(ids,apikey, request_url, store))
        threads.append(t)

    # start the threads
    [ t.start() for t in threads ]
    # wait for the threads to finish
    [ t.join() for t in threads ]
    return store
    
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#