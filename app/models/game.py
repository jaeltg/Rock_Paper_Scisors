from app.models.player import Player

player_1 = Player("Emily", "Paper")
player_2 = Player("Rachel", "Paper")

players = [player_1, player_2]

def game_result(move1, move2):
    if move1.lower()  == "paper" and move2.lower()  == "scissors":
        return f"{player_2.name} wins with SCISSORS!"
    elif move1.lower()  == "scissors" and move2.move.lower()  == "paper":
        return f"{player_1.name} wins with SCISSORS!"
    elif move1.lower()  == "paper" and move2.lower()  == "rock":
        return f"{player_1.name} wins with PAPER"
    elif move1.lower()  == "rock" and move2.lower()  == "paper":
        return f"{player_2.name} wins with PAPER"
    elif move1.lower()  == "rock" and move2.lower()  == "scissors":
        return f"{player_1.name} wins with ROCK"
    elif move1.lower()  == "scissors" and move2.lower()  == "rock":
        return f"{player_2.name} wins with ROCK"   
    elif move1.lower()  == move2.lower():
        return f"It's a Tie!"   

result = game_result(player_1.choice, player_2.choice)
                 
print(result)
