import random
num = random.randint(0,9)
turn = 0
for i in range(10):
    guess = int(input("Player " + str(turn+1) + " make your guess: "))
    if(guess==num):
        print("Player " + str(turn+1) + " got it!!\nThe answer is " + str(guess))
        break
    turn = not turn
else:
    print("Sorry!\nYou couldn't guess in 10 turns\nThe answer was " + str(num))