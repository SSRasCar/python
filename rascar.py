import RPi.GPIO as io
import sys, termios, tty, time

pin = [3,5,7,8]

io.setmode(io.BOARD)
for i in range(len(pin)):
    io.setup(pin[i],io.OUT)

def forward():
    io.output(pin[0], True)
    time.sleep(1)
    io.output(pin[0], False)
    print "forward"

def reverse():
    io.output(pin[1], True)
    time.sleep(1)
    io.output(pin[1], False)
    print "reverse"

def left():
    io.output(pin[2], True)
    time.sleep(1)
    io.output(pin[2], False)
    print "left"

def right():
    io.output(pin[3], True)
    time.sleep(1)
    io.output(pin[3], False)
    print "right"


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

io.cleanup()
