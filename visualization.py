import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('result.csv')
bins = np.arange(43.5,88.1,0.5) #https://hashcode.co.kr/questions/646/range%EC%9D%98-step%EC%97%90%EC%84%9C-%EC%A0%95%EC%88%98-%EB%A7%90%EA%B3%A0-float%EC%9D%84-%EC%93%B0%EB%A0%A4%EB%A9%B4

cnt = data['win_rate'].value_counts(bins=bins, sort=False) #bins범위마다 체크.

cnt_list = cnt.values.tolist()  #https://note.nkmk.me/en/python-pandas-list/
bins = bins.tolist()

print(bins.type())
print(cnt_list.type())
