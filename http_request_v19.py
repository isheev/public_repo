import requests, json

def handle(data): # data come as string 
    params_json = json.loads(data)
    result = requests.get(params_json['link'], verify=False) # verify=False
    return json.dumps({"script_ver": 19, "params": params_json, "response": json.loads(result.content.decode("utf-8"))})
