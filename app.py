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

    # Extract game data
    game_data = []
    for game in tst['scoreboard']['games']:
        home_team = game['homeTeam']['teamName']
        away_team = game['awayTeam']['teamName']
        game_time = game['gameStatusText']
        game_location = game['homeTeam']['teamCity']
        
        game_data.append({'home_team': home_team, 'away_team': away_team, 'game_time': game_time, 'game_location': game_location})
        
    # Render template with game data
    return render_template('index.html', games=game_data)


if __name__ == '__main__':
    app.run(debug=True)