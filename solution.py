import time
import mypackage.demo as mp

name = "Addison"
print("Welcome to Human Behavior Prediction by %s" % (name))

while(True):
    inputDiff = input("Choose the type of game(1: Easy, 2: Difficult): ")
    try:
        difficulty = int(inputDiff)
        if(difficulty==1 or difficulty==2):
            break
        else:
            print("Please input difficulty as per instructions. (1/2)")

    except ValueError:
        print("Please input valid integer as difficulty")

while(True):
    inputN = input("Enter the number of moves: ")
    try:
        n = int(inputN)
        break
    except ValueError:
        print("Please input valid integer as number of moves")


t00 = t01 = t10 = t11 = 0

# Difficult calculation of the move
def calcMoveDiff(prev, xi):
    global t00, t01, t10, t11
    xi, c = mp.calcMoveEasy(xi)
    if(prev==0):
        if(t10 > t00):
            return xi, 1
        elif(t10 < t00):
            return xi, 0
        elif(t10 == t00):
            return xi, c
    elif(prev==1):
        if(t11 > t01):
            return xi, 1
        elif(t11 < t01):
            return xi, 0
        elif(t11 == t01):
            return xi, c    
    return None


while(True):
    t00 = t01 = t10 = t11 = 0
    prev = -1
    user_score = 0
    comp_score = 0
    xi = 1234
    # xi = round(time.time()*1000)

    for i in range(n):

        if(difficulty==1):
            xi, computer_move = mp.calcMoveEasy(xi)
        else:
            if(i<2):
                xi, computer_move = mp.calcMoveEasy(xi)
                # computer_move = 0
            else:
                xi, computer_move = calcMoveDiff(prev, xi)

        # user_move = int(input("Choose your move number %d (0 or 1): " % (i+1)))
        while(True):
            inputUserMove = input("Choose your move number %d (0 or 1): " % (i+1))
            try:
                user_move = int(inputUserMove)
                if(user_move==1 or user_move==0):
                    break
                else:
                    print("Please input user move as per instructions. (0/1)")
                    
            except ValueError:
                print("Please input valid integer as user move")
        
        if(user_move==0):
            if(prev==0):
                t00 += 1
            elif(prev==1):
                t01 += 1
        elif(user_move==1):
            if(prev==0):
                t10 += 1
            elif(prev==1):
                t11 += 1
        prev = user_move

        if(user_move==computer_move):
            msg = "Computer"
            comp_score += 1
        else:
            msg = "Player"
            user_score += 1
        print("player = %d machine = %d - %s wins!" % (user_move, computer_move, msg))
        print("PLAYER: ", "*"*user_score)
        print("COMPUTER: ", "*"*comp_score)
        print("---")

    game_type = ""
    if(difficulty==1):
        game_type = "Easy"
    elif(difficulty==2):
        game_type = "Difficult"

    res_msg = ""
    if(user_score > comp_score):
        res_msg = "You won!"
    elif(user_score < comp_score):
        res_msg = "The COMPUTER won!"
    else:
        res_msg = "It was a tie!"

    print("%s game is over, final score: player %d - %d computer - %s" % (game_type, user_score, comp_score, \
                                                                          res_msg))
        
    while(True):
        check = input("Do you want to play again? (Y/N): ")
        if(check=="Y" or check=="N"):
            break
        else:
            print("Please try again. Enter valid option to continue or exit.")
        
    if(check.lower()=="n"):
        print("Thanks for playing!")
        break