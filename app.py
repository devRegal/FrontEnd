from flask import Flask, render_template
from datetime import datetime
from nba_api.stats.endpoints import scoreboardv2, boxscoretraditionalv2

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.today().strftime('%Y-%m-%d')
    scoreboard = scoreboardv2.ScoreboardV2(game_date=today).game_header.get_data_frame()
    scoreboard['GAME_DATE_EST'] = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%S').strftime('%B %d, %Y') for date in scoreboard['GAME_DATE_EST']]
    print(scoreboard.keys)
    return render_template('index.html', scoreboard=scoreboard)

if __name__ == '__main__':
    app.run(debug=True)
