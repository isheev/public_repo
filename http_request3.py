import requests, json

def handle(data):
    resutl = requests.get(data['link'], verify=False) # verify=False
    #resutl = requests.get("https://vpnff-hub.mydom.top:8443/4hGm1o5STzTxYwfn/run_cmd?cmd=hostname", verify=False) # verify=False
    #return json.dumps({"test": "2"})
    return json.dumps({"params": data, "version": "3", "response": resutl.content.decode("utf-8")})
    #return json.loads(resutl.content.decode("utf-8"))
