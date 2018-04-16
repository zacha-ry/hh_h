#enconding=utf-8
import socket
client_so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = socket.gethostname()
#host = '172.16.252.6'
host = '39.108.223.47'
port = 8080
client_so.connect((host,port))
request = 'POST /XY HTTP/1.1\r\n\r\n{[{\'mac\':\'0:0:1:1\',\'d1\':4.0,\'d2\':5.0,\'d3\':3.0}]}'

request_s = 'GET /XY HTTP/1.1\r\nMAC:0:0:0:1\r\n'
print request
client_so.send(request_s)
data = client_so.recv(1000)
print data
