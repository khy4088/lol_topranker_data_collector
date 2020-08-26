import requests
import numpy as np
import pandas as pd
import json

with open('./champion_ko_KR.json', 'r', encoding='UTF-8') as f:
    json_dict = json.load(f)

print(json_dict)


for author in json_dict['data']:
    print(json_dict['name'])