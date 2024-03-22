import json
import random

with open("keys.json") as token_data:
    tokens = json.load(token_data)
    
def get_keys():
    return tokens
    
# Should only return weapons that aren't shields or bows/arrows
def get_random_weapon():
    with open("weapons.json") as weapon_data:
        weapons = json.load(weapon_data)
        
        random_index = random.range(0, len(weapons))
        
        return weapons[random_index]

# Should only return weapons that aren't shields or bows/arrows
def get_specific_weapon(weapon_name):
    if weapon_name is None:
        return
    
    with open("weapons.json") as weapon_data:
        weapons = json.load(weapon_data)
        
        try:
            return weapons[weapon_name]
        except:
            print (f"{weapon_name} not found")