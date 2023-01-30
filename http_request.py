import requests

#resutl = requests.get('https://deepholevpn-cl1-hub.mydom.top:8001/4hGm1o5STzTxYwfn/run_cmd?cmd=ls', verify=False)
#print(resutl.content)

def handle(data):
    resutl = requests.get(data['url'], verify=False)
    return resutl.content

params = {"url":"https://deepholevpn-cl1-hub.mydom.top:8001/4hGm1o5STzTxYwfn/run_cmd?cmd=ls"}
r = handle(params)
print(r)
