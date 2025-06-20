import pandas as pd
import matplotlib.pyplot as plt

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

import requests

dict_ = {'a':[11, 21, 31], 'b':[12, 22, 32]}
df = pd.DataFrame(dict_)

print(f"type_df: {type(df)}\nmean: {df.mean()}\n")

def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

nba_teams = teams.get_teams()
nba_w_teams = teams.get_wnba_teams()

dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)
print(df_teams.head())

dict_nba_w_teams = one_dict(nba_w_teams)
df_w_teams = pd.DataFrame(dict_nba_w_teams)
print(df_w_teams.head())

df_warriors = df_teams[df_teams['nickname']=='Warriors']
print(df_warriors)

id_warriors = df_warriors[['id']].values[0][0]
print(id_warriors)

# Making an API call to get and assign the object
#gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
#gamefinder.get_json()
#games = gamefinder.get_data_frames()[0]
#games.head()

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):        #will download the dataframe from the API call
    response = requests.get(url)
    if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)

download(filename, "GoldenState.pkl")

file_name = "GoldenState.pkl"
games = pd.read_pickle(file_name)   #pandas to pickle
print(f"games = \n{games.head()}")

games_home = games[games['MATCHUP']=='GSW vs. TOR']
games_away = games[games['MATCHUP']=='GSW @ TOR']

print(games_home['PLUS_MINUS'].mean())
print(games_away['PLUS_MINUS'].mean())

fig, ax = plt.subplots()

games_away.plot(x = 'GAME_DATE', y = "PLUS_MINUS", ax=ax)
games_home.plot(x = 'GAME_DATE', y = "PLUS_MINUS", ax=ax)
ax.legend(["away", "home"])
plt.show()