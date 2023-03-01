from nba_api.live.nba.endpoints import scoreboard
import json
# Today's Score Board
games = scoreboard.ScoreBoard()

# json
games.get_json()

# dictionary
games.get_dict()

tst = json.loads(games.get_json())

# print(json.dumps(tst['scoreboard'], indent=4))
# print(tst['scoreboard']['games'])
# print(tst['scoreboard']['games'][0])

print(json.dumps(tst['scoreboard']['games'][0], indent=4))