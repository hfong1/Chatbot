import socket
from Settings import HOST, PORT, PASS, NICK, CHANNEL

def openSocket():
	s = socket.socket()
	s.connect((HOST, 6667))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + NICK + "\r\n")
	s.send("JOIN #" + CHANNEL + "\r\n")
	return s

	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(messageTemp + "\r\n")
	print "Sent: " + messageTemp

def ping(s):
	s.send("PONG\r\n")
	print "PONG"