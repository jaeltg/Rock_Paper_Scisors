from flask import render_template, request, redirect
from app import app
from app.models.game import Game 
from app.models.player import Player

@app.route('/')
def welcome():
    return render_template('welcome.html', title="Welcome!")

@app.route('/play')
def index():
    game = Game("RPS")
    return render_template('index.html', title="Play!", players=game.players, results=game.results)

@app.route('/play', methods=['POST'])
def create():
    player1_name = request.form["name1"]
    player1_choice = request.form["choice1"]
    player2_name = request.form["name2"]
    player2_choice = request.form["choice2"]
    player1 = Player(player1_name, player1_choice)
    player2 = Player(player2_name, player2_choice)
    game = Game("RPS")
    game.add_player(player1)
    game.add_player(player2)
    result = game.game_result(player1, player2, player1.choice, player2.choice)
    game.add_result(result)
    return redirect('/play')

@app.route('/playpc')
def indexPC():
    game = Game("RPS")
    return render_template('playpc.html', title="Play against PC!", players=game.players, results=game.results)

@app.route('/playpc', methods=['POST'])
def createPC():
    player1_name = request.form["name1"]
    player1_choice = request.form["choice1"]
    player1 = Player(player1_name, player1_choice)
    game = Game("RPS")
    game.add_player(player1)
    pc_player = game.pc_player()
    game.add_player(pc_player)
    result = game.game_result(player1, pc_player, player1.choice, pc_player.choice)
    game.add_result(result)
    print(pc_player)
    return redirect('/playpc')
        