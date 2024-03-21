import json

with open('keys.json') as keys:
    tokens = json.load(keys)
    
def get_keys():
    return tokens