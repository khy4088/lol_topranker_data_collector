import csv
import glob
import pandas as pd 


file_list = glob.glob('*.csv')
merge_file = 'merged_user_list.csv'
try:
    file_list.remove('merged_user_list.csv')
except ValueError:
    print("no file in folder")

with open(merge_file, 'w', encoding='UTF-8') as f: 
    for i, file in enumerate(file_list):
    
        if i == 0 :
            with open(file, 'r', encoding='UTF-8') as f2:
                while True:
                    line = f2.readline()

                    if not line:
                        break
                    
                    f.write(line)

            file_name = file.split('\\')[-1]
            print(file.split('\\')[-1] + ' write complete...')

        else: 
            with open(file, 'r', encoding='UTF-8') as f2:
                n = 0 #csv 파일의 row를 체크하기 위한 변수 
                while True: 
                    line = f2.readline() # 2.merge 대상 파일의 row 1줄을 읽어서 
                    if n != 0: # 첫번째 row(헤더)를 제외한 
                        f.write(line) # 3.읽은 row 1줄을 merge할 파일에 쓴다. 

                    if not line: # row가 없으면 해당 csv 파일 읽기 끝 
                        break 
                    
                    n += 1
            file_name = file.split('\\')[-1] 
            print(file.split('\\')[-1] + ' write complete...')

print('>>> All file merge complete...')



merged = pd.read_csv(merge_file)
merged['win_rate'] = 100 *  merged['wins'] / (merged['wins'] + merged['losses']) 
print(a)

a.to_csv("./result.csv")