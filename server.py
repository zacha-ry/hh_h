#encoding=utf-8
import socket
from deal_request import deals_request 
import multiprocessing
server_so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = socket.gethostname()
host = '' #服务器的ip地址
print host
port = 8080 #服务器的端口号
#套接字初始化 打开 绑定套接字 监听
server_so.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_so.bind((host,port))
server_so.listen(10)
#进程回调函数
#处理每个客服端的请求
def worker(args):
	rcv_data = args.recv(1000) #客服端的数据
	respond_body = str(deals_request(rcv_data)) #处理客服端的请求 返回的是要发给客服端的数据
	print type(respond_body)
	print 'body:',respond_body
	respond_line = 'HTTP/1.1 200 OK\r\n'
	respond_head = 'Server:myserver\r\n'
	respond = respond_line + respond_head +'\r\n' +str(respond_body)
	#	HTTP/1.1 200 OK
	#	Server:myserver
	#	
	#	respond_body的内容

	print type(respond_body)		
	args.send(bytes(respond))
	args.close();	
while True:
	client_so,addr = server_so.accept(); #有客服连接时 分配一个套接字
	#创建一个进程给每个客服端
	p = multiprocessing.Process(target = worker, args = (client_so,))
	p.start()

