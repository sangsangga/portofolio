import random
import sys

num_target = random.randint(1,20) # initate target number
print("Guess the number between 1 and 20")


for i in range(10,0,-1):
    print(f"You have {i} guesses")
    guess = int(input())
    checker = guess == num_target # checking answer

    if checker:
        print(f"Congratulations you are correct with {i} attemps left!")
        sys.exit()
    else:
        residual = guess - num_target # checking error
        if residual < 0:
            print("Too low!")
        else:
            print("Too high!")


