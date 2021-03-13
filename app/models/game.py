from app.models.player import Player

class Game:
    def __init__(self, name, players = [], results = []):
        self.name = name
        self.players = players
        self.results  = results

    def add_player(self, player):
        self.players.append(player)

    def add_result(self, result):
        self.results.append(result)

    def game_result(self, player1, player2, choice1, choice2):
        if choice1.lower()  == "paper" and choice2.lower()  == "scissors":
            return f"{player2.name} wins with SCISSORS!"
        elif choice1.lower()  == "scissors" and choice2.lower()  == "paper":
            return f"{player1.name} wins with SCISSORS!"
        elif choice1.lower()  == "paper" and choice2.lower()  == "rock":
            return f"{player1.name} wins with PAPER!"
        elif choice1.lower()  == "rock" and choice2.lower()  == "paper":
            return f"{player2.name} wins with PAPER!"
        elif choice1.lower()  == "rock" and choice2.lower()  == "scissors":
            return f"{player1.name} wins with ROCK!"
        elif choice1.lower()  == "scissors" and choice2.lower()  == "rock":
            return f"{player2.name} wins with ROCK!"   
        elif choice1.lower()  == choice2.lower():
            return f"It's a TIE!"   
