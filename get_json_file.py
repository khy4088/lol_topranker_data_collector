from urllib import request

champion_en_US = "champion_en_US.csv"
champion_ko_KR = "champion_ko_KR.csv"
en_US_data = "http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json"
ko_KR_data = "http://ddragon.leagueoflegends.com/cdn/10.16.1/data/ko_KR/champion.json"

usdata = request.urlopen(en_US_data).read()
krdata = request.urlopen(ko_KR_data).read()

with open(usdata, mode="wb") as f:
    f.write(usdata)

with open(krdata, mode="wb") as f:
    f.write(usdata)