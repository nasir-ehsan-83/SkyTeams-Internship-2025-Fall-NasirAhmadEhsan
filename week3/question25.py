def guess_number_game(secret, guess):
    if guess == secret:
        return "Correct"
    elif guess < secret:
        return "Too Low"
    else:
        return "Too High"
