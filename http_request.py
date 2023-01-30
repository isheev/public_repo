import requests, json

def handle(data):
    resutl = requests.get(data['link'], verify=False) # verify=False
    return json.loads(resutl.content.decode("utf-8"))
