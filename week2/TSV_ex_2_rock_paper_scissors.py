def rock_paper_scissors(symbol_1: str, symbol_2: str) -> str:
    choices = ["rock", "paper", "scissors", "well"]
    if not (symbol_1 in choices) or not (symbol_2 in choices):
        return "incorrect input"
    if symbol_1 == symbol_2:
        return "tie"
    if symbol_1 == "rock" and symbol_2 == "scissors":
        return "player_1"
    elif symbol_1 == "well" and ((symbol_2 == "rock") or (symbol_2 == "scissors")):
        return "player_1"
    elif symbol_1 == "scissors" and symbol_2 == "paper":
        return "player_1"
    elif symbol_1 == "paper" and ((symbol_2 == "rock") or (symbol_2 == "well")):
        return "player_1"
    elif symbol_2 == "rock" and symbol_1 == "scissors":
        return "player_2"
    elif symbol_2 == "well" and ((symbol_1 == "rock") or (symbol_1 == "scissors")):
        return "player_2"
    elif symbol_2 == "scissors" and symbol_1 == "paper":
        return "player_2"
    elif symbol_2 == "paper" and ((symbol_1 == "rock") or (symbol_1 == "well")):
        return "player_2"
        pass
