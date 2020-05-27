import random

guess = 3

def guessing_game():

    input("Let's play the guessing game! I'm going to ask you to select a range to guess between.\n\
Press any key to start! ")

    min_ = input("What's the beginning number of the range? ")
    max_ = input("What's the max number of the range? ")
    global guess_num
    guess_num = range(int(min_), int(max_))
    guess_num = random.choice(guess_num)

    while(guess):

        g1 = input("You've got {} tries! What's your guess? \n" .format(guess))
        check_guess(int(g1))


def check_guess(x):

    global guess
    
    if x == guess_num:
        print("You won!! Nice job")
        guess = 0

    elif x > guess_num:
        guess -= 1
        if(guess):
            print("Too high! Try again, you have {} guesses remaining" .format(guess))
        
        else: check_loss()
            
    else:
        guess -= 1
        if(guess):
            print("Too low! Try again, you have {} guesses remaining" .format(guess))

        else: check_loss()
        
def check_loss():
    global guess
    
    if guess == 0:
        play = input('You lost! Sorry :( Press L if you want to play again, or anything else to quit! ')

        if play == 'L' or play == 'l':
            guess = 3
            guessing_game()
            
guessing_game()
