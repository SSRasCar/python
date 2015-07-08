import RPi.GPIO as io
import sys, termios, tty, time

pin = [3,5,7,8]

io.setmode(io.BOARD)
for i in range(len(pin)):
    io.setup(pin[i],io.OUT)

#w
def forward():
    io.output(pin[0], True)
    print "forward"

#s
def reverse():
    io.output(pin[1], True)
    print "reverse"

#a
def left():
    io.output(pin[2], True)
    time.sleep(0.1)
    io.output(pin[2], False)
    print "left"

#d
def right():
    io.output(pin[3], True)
    ime.sleep(0.1)
    io.output(pin[2], False)
    print "right"

#e
def stop():
    for i in range(len(pin)):
        io.output(pin[i],False)    

#x for exit
def cleanup():
    stop()
    io.cleanup()

if __name__ == "__main__":
    try:
        forward()
        while True:
            time.sleep(1)
    finally:
        print "Cleanup"
        stop()
        cleanup()
