from flask import Flask, render_template
from nba_api.live.nba.endpoints import scoreboard
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Today's Score Board
    games = scoreboard.ScoreBoard()

    # Convert JSON to Python dictionary
    tst = json.loads(games.get_json())

    tst2 = json.dumps(tst['scoreboard']['games'][0]['homeTeam']['periods'], indent=4)

    print(tst2)
    # Extract game data
    game_data = []
    for game in tst['scoreboard']['games']:
        home_team = game['homeTeam']['teamName']
        away_team = game['awayTeam']['teamName']
        game_time = game['gameStatusText']
        game_location = game['homeTeam']['teamCity']
        current_score = game['homeTeam']['periods']
        total_score = sum(period['score'] for period in current_score)
        away_score = game['awayTeam']['periods']
        away_team_score = sum(period['score'] for period in away_score)
        print('HERE IS THE TOTAL CURRENT SCORE : ' + str(total_score))
        print('AWAY TEAM SCORE : ' + str(away_team_score))


        game_data.append({'home_team': home_team, 'away_team': away_team, 'game_time': game_time, 'game_location': game_location, 'home_score' : total_score, 'away_score' : away_team_score})
        
    # Render template with game data
    return render_template('index.html', games=game_data)


if __name__ == '__main__':
    app.run(debug=True)