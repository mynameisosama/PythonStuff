import random

attempts = 0
num = int(random.randint(1,9))
while True:
    guess = raw_input("Enter your guess ('exit' to stop): ")
    attempts+=1
    if guess.lower()=='exit':
        break
    else:
        guess = int(guess)
        if guess==num:
            print "exactly right!"
            print "in %d attempt(s)" % attempts
            attempts = 0
            num = int(random.randint(1,9))
        elif guess < num:
            print "too low"
        else:
            print "too high"
