from flask import render_template, request, redirect
from app import app
from app.models.game import players, add_player, game_result, add_result, results
from app.models.player import Player

@app.route('/')
def welcome():
    return render_template('welcome.html', title="Welcome!")

@app.route('/play')
def index():
     return render_template('index.html', title="Play!", players=players, results=results)

@app.route('/play', methods=['POST'])
def create():
    player1_name = request.form["name1"]
    player1_choice = request.form["choice1"]
    player2_name = request.form["name2"]
    player2_choice = request.form["choice2"]
    player1 = Player(player1_name, player1_choice)
    player2 = Player(player2_name, player2_choice)
    add_player(player1)
    add_player(player2)
    result = game_result(player1, player2, player1.choice, player2.choice)
    add_result(result)
    return redirect('/play')
    