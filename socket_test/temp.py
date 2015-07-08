import sys, termios, tty, time

#w
def forward():
    print "forward"

#s
def reverse():
    print "reverse"

#a
def left():
    print "left"

#d
def right():
    print "right"

#e
def stop():
    print "stop"
#x for exit
def cleanup():
    stop()

if __name__ == "__main__":
    try:
        forward()
        while True:
            time.sleep(1)
    finally:
        print "Cleanup"
        stop()
        cleanup()
