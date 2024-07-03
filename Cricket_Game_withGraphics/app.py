from flask import Flask, render_template, request, redirect, url_for
from cricket import Cricket

app = Flask(__name__)
cricket = Cricket()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_match', methods=['POST'])
def start_match():
    team1 = request.form['team1']
    team2 = request.form['team2']
    over = request.form['over']
    
    try:
        over = int(over)
    except ValueError:
        return redirect(url_for('index', error="Please enter a valid number of overs."))
    
    try:
        cricket.chooseTeam(team1, team2)
        cricket.selectOver(over)
        result = cricket.playMatch()
        return render_template('result.html', cricket=cricket, result=result, enumerate=enumerate)
    except ValueError as e:
        return redirect(url_for('index', error=str(e)))

if __name__ == "__main__":
    app.run(debug=True)
