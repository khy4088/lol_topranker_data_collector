import requests
import numpy as np
import pandas as pd
import json
import csv

with open('./champion_ko_KR.json', 'r', encoding='UTF-8') as f:
    json_dict = json.load(f)

print(type(json_dict))
champ_data = json_dict['data']
#print(champ_data)
champ_list = []
for value in champ_data.keys():
    champ_list.append(value)

column = list(champ_data[champ_list[0]].keys())
print(column)

csv_data = pd.DataFrame(columns=column)
print(csv_data)
csv_data.to_csv('champ_data.csv')

f = open("./champ_data.csv", 'w', encoding='UTF-8')
writer = csv.writer(f)

writer.writerow(column)
for i in range(len(champ_list)):
    writer.writerow(list(champ_data[champ_list[i]].values()))

f.close()