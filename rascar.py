#import RPi.GPIO as io
import sys, termios, tty, time

#pin = [3,5,7,8]

#io.setmode(io.BOARD)
#for i in pin:
#    io.setup(pin[i],io.out)

def forward():
    io.output(pin[0], True)
    time.sleep(1)
    io.output(pin[0], False)
    time.sleep(1)
    print "forward"

def left():
    print "left"

def right():
    print "right"

def reverse():
    print "reverse"

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    char = getch()
    print "this is the " + char
    if(char == "x"):
        break
    if char == "a":
        left()
    if char == "d":
        right()
    if char == "w":
        forward()
    if char == "s":
        reverse()