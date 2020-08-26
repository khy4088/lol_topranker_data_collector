import requests
import numpy as np
import pandas as pd
import json

with open('./champion_ko_KR.json', 'r', encoding='UTF-8') as f:
    json_dict = json.load(f)

print(type(json_dict))
champ_data = json_dict['data']
#print(champ_data)
champ_list = []
for value in champ_data.keys():
    champ_list.append(value)

print(champ_list)