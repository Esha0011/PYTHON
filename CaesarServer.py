import socket
soc=socket.socket()
soc.bind("",14567)
soc.listen(10)
c=soc.accept()
