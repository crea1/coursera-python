# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = []
ball_vel = []
paddle_vel = 4
paddle1_pos = [PAD_WIDTH / 2, HEIGHT / 2]
paddle2_pos = [WIDTH - (PAD_WIDTH / 2), HEIGHT / 2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# Get new paddle position if inside canvas
def get_paddle_pos(pos, vel):
    next_pos = pos + vel
    if (next_pos + PAD_HEIGHT <= HEIGHT and next_pos >= 0):
        return next_pos
    else:
        return pos
# Reflects ball from paddle and increases velocity by 10%
def reflect_ball():
    ball_vel[0] = ball_vel[0] * -1
    ball_vel[0] = ball_vel[0] * 1.1
    ball_vel[1] = ball_vel[1] * 1.1
    

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    vel_x = random.randrange(2, 4)
    vel_y = random.randrange(1, 3) * -1
    if (direction == LEFT):
        vel_x = vel_x * -1
        
    ball_vel = [vel_x, vel_y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    if (ball_pos[1] >= (HEIGHT - 1 - BALL_RADIUS) or ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = ball_vel[1] * -1
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] = get_paddle_pos(paddle1_pos[1], paddle1_vel)
    paddle2_pos[1] = get_paddle_pos(paddle2_pos[1], paddle2_vel)
    
    # draw paddles
    canvas.draw_line(paddle1_pos, (paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT), PAD_WIDTH, 'White')
    canvas.draw_line(paddle2_pos, (paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT), PAD_WIDTH, 'White')
    
    # determine whether paddle and ball collide    
    if (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH):
        if (ball_pos[1] > paddle1_pos[1] and ball_pos[1] < paddle1_pos[1] + PAD_HEIGHT):
            reflect_ball()
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif (ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH):
         if (ball_pos[1] > paddle2_pos[1] and ball_pos[1] < paddle2_pos[1] + PAD_HEIGHT):
            reflect_ball()
         else:
            score1 += 1
            spawn_ball(LEFT)
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 4, HEIGHT / 5), 48, 'White')
    canvas.draw_text(str(score2), (WIDTH / 4 * 3 -24, HEIGHT / 5), 48, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if ('W' == chr(key)):
        paddle1_vel = -paddle_vel
    elif ('S' == chr(key)):
        paddle1_vel = paddle_vel
    elif (38 == key):
        paddle2_vel = -paddle_vel
    elif (40 == key):
        paddle2_vel = paddle_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if ('W' == chr(key) or 'S' == chr(key)):
        paddle1_vel = 0
    elif(38 == key or 40 == key):
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset game', new_game)


# start frame
new_game()
frame.start()

