# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

secret_number = 0
upper_range = 100
allowed_guesses = 7

def new_game():
    global secret_number
    secret_number = random.randrange(0, upper_range)
    reset_allowed_guesses()
    print ''
    print 'New game. Range is from 0 to', upper_range
    print 'Number of remaining guesses is', allowed_guesses
    
def reset_allowed_guesses():
    global allowed_guesses
    if upper_range == 100: 
        allowed_guesses = 7
    else: 
        allowed_guesses = 10

# define event handlers for control panel
def range100():
    global upper_range, allowed_guesses
    upper_range = 100
    new_game()   

def range1000():
    global upper_range, allowed_guesses
    upper_range = 1000
    new_game()
    
def input_guess(guess):
    global allowed_guesses
    allowed_guesses = allowed_guesses -1
    g = int(guess)
            
    print ''
    print 'Guess was ' + guess
    print 'Number of remaining guesses is', allowed_guesses
    
    if g == secret_number:
        print 'Correct'
        new_game()
    elif allowed_guesses == 0:
        print 'You ran out of guesses.  The number was', secret_number
        new_game()
    elif g < secret_number:
        print 'Higher'
    elif g > secret_number:
        print 'Lower'


    
# create frame
frame = simplegui.create_frame('Testing', 100, 200)

# register event handlers for control elements and start frame
btn100 = frame.add_button('Range: 0 - 100', range100)
btn1000 = frame.add_button('Range: 0 - 1000', range1000)
inp = frame.add_input('Enter guess', input_guess, 50)

# call new_game 
new_game()


