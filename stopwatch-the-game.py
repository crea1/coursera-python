# template for "Stopwatch: The Game"
import simplegui
import time
# define global variables
time_passed = 0
successful_stops = 0
total_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    mi = str(t % 10)
    s = str((t / 10) % 60)
    m = str((t / 600) % 60)
    if len(s) < 2:
        s = '0' + s
    return m + ':' + s + '.' + mi

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    if timer.is_running():
        global total_stops, successful_stops
        total_stops += 1
        timer.stop()        
        if time_passed % 10 == 0:
            successful_stops += 1
        
def reset():
    global time_passed, total_stops, successful_stops
    time_passed = 0
    total_stops = 0
    successful_stops = 0
    timer.stop()
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time_passed
    time_passed += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time_passed), (40, 65), 50, '#FFF')
    canvas.draw_text(str(successful_stops) + '/' + str(total_stops), (170,15), 16, 'Green')
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 200, 100, 100)

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start, 50)
frame.add_button('Stop', stop, 50)
frame.add_button('Reset', reset, 50)

# start frame
frame.start()

