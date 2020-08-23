import pandas as pd 

file = 'merged_user_list.csv'

a = pd.read_csv(file)
a['win_rate'] = 100 *  a['wins'] / (a['wins'] + a['losses']) 
print(a)

a['win_rate'] = round(a['win_rate'], 3)
print(a)

a.to_csv("./result.csv")