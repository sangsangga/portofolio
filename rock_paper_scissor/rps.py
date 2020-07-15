import random
import sys

def checking_answer(player,enemy):
    if player.lower() == "p" and enemy.lower() =="r":
        return "win"
    elif player.lower() == "s" and enemy.lower() =="p":
        return "win"
    elif player.lower() == "r" and enemy.lower() == "s":
        return "win"
    elif player.lower() == enemy.lower():
        return "draw"
    return "lose"
def checking_input(input):
    if input in ["r","p","s"]:
        return True
    return False

win = 0
lose = 0
draw = 0

while True:
    print(f"Wins: {win} Lose: {lose} Draw:{draw}")
    print("=======================================")
    print("\n")
    num_rand = random.randint(0,2)
    choices = ["r","p","s"]
    print("Rock('r'),Scissor('s'),Paper('p'),Quit('q')")
    guess = input("Input your move:")
    checker = checking_input(guess.lower())
    enemy_guess = choices[num_rand]
    if guess.lower()=="q":
        sys.exit()
    if checker:
        result = checking_answer(guess,enemy_guess)
        if result == "win":
            win +=1
        elif result =="lose":
            lose +=1
        else:
            draw +=1

    
    

    




