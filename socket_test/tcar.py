import socket
import sys
import temp as car
from thread import *

HOST = ''
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((HOST,PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

s.listen(10)

def clientthread(conn):
	while True:
		data = conn.recv(1024)

		if not data:
			print "Socket closed"
			break

		data = ''.join(data.split())

		if data == "w":
			car.forward()
		if data == "s":
			car.reverse()
		if data == "a":
			car.left()
		if data == "d":
			car.right()
		if data == "e":
			car.stop()
		#if data == "x":
		#	car.cleanup()

try:
	while True:
		print "Waiting.."

		conn, addr = s.accept()
		print 'Connected with ' + addr[0] + ':' + str(addr[1])

		start_new_thread(clientthread, (conn,))

finally:
	print "Exiting"
	try:
		car.stop()
	except:
		pass

	s.close()
	time.sleep(0.5)
	car.cleanup()












