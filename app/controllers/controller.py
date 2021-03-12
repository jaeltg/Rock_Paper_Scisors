from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import Player

@app.route('/rock/scissors')
def index():
    return "Player 1 wins with rock"