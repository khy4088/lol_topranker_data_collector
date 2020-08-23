import numpy as np
import pandas as pd
import requests

API_KEY = open('API_KEY.txt', 'r').readline()

grandmaster = 'https://kr.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key=' + API_KEY
challenger = 'https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=' + API_KEY
master = 'https://kr.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key=' + API_KEY


def get_data(tier,link):
    r = requests.get(link)#그마데이터 호출
    file_name = tier + '_data.csv'
    league_df = pd.DataFrame(r.json())
    league_df.reset_index(inplace=True)#수집한 그마데이터 index정리
    league_entries_df = pd.DataFrame(dict(league_df['entries'])).T #dict구조로 되어 있는 entries컬럼 풀어주기
    league_df = pd.concat([league_df, league_entries_df], axis=1) #열끼리 결합
    league_df = league_df.drop(['index', 'queue', 'name', 'leagueId', 'entries', 'rank'], axis=1)
    league_df.info()
    league_df.to_csv(file_name,index=False,encoding = 'UTF-8')#중간저장


get_data('challenger', challenger)
get_data('grandmaster', grandmaster)
get_data('master', master)
