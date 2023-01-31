import requests, json

def handle(data): # data come as string 
    data_json = json.loads(data)
    result = requests.get(data_json['link']) # verify=False
    #result = requests.get("https://vpnff-hub.mydom.top:8443/4hGm1o5STzTxYwfn/run_cmd?cmd=hostname", verify=False) # verify=False
    #return json.dumps({"test": "2"})
    return str(json.dumps({"params": json.loads(data), "version": "15", "response": json.loads(result.content.decode("utf-8"))}))
    #return json.loads(result.content.decode("utf-8"))
