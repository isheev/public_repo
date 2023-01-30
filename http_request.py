import requests, json

#resutl = requests.get('https://deepholevpn-cl1-hub.mydom.top:8001/4hGm1o5STzTxYwfn/run_cmd?cmd=ls', verify=False)
#print(resutl.content)

def handle(data):
    resutl = requests.get("https://vpnff-hub.mydom.top:8443/4hGm1o5STzTxYwfn/run_cmd?cmd=ls") # verify=False
    return json.loads(resutl.content.decode("utf-8"))
