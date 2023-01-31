import requests, json

def handle(data): # data come as string 
    params_json = json.loads(data)
    result = requests.get(params_json['link'], verify=False) # verify=False
    #result = requests.get("https://vpnff-hub.mydom.top:8443/4hGm1o5STzTxYwfn/run_cmd?cmd=hostname", verify=False) # verify=False
    #return json.dumps({"test": "2"})
    return json.dumps({"params": params_json, "version": 18, "response": json.loads(result.content.decode("utf-8"))})
    #return json.loads(result.content.decode("utf-8"))
