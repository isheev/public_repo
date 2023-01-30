import requests, json
import base64

def handle(data):
    resutl = requests.get(base64.b64decode(data['url']), verify=False) # verify=False
    return json.loads(resutl.content.decode("utf-8"))
