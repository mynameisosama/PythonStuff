while True:
    start = raw_input("Do You Want to Start a New Game? (Y/N): ")
    if start.lower() == 'y':
        player1 = int(raw_input("Player1 -> 1-Rock, 2-Paper, 3-Scissor: "))
        player2 = int(raw_input("Player2 -> 1-Rock, 2-Paper, 3-Scissor: "))
        if player1 == player2:
            print "Draw!"
        else:
            if player1==1:
                if player2==2:
                    print "Player 2 Wins!"
                else:
                    print "Player 1 Wins!"
            elif player1==2:
                if player2==3:
                    print "Player 2 Wins!"
                else:
                    print "Player 1 Wins!"
            else:
                if player2==1:
                    print "Player 2 Wins!"
                else:
                    print "Player 1 Wins!"
    else:
        break
