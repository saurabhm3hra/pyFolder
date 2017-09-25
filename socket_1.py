import socket
import xlrd as xls

socket1 = socket.socket()
port = 15555
socket1.bind(("127.0.0.1", port))
socket1.listen()

print "" + math.log(10, 10)

while True:
    c, addr = socket1.accept()     # Establish connection with client.
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    c.close()                # Close the connection
