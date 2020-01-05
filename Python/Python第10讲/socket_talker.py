import socket      #导入socket模块

ip_port = ('127.0.0.1',8010) #定义元组
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建客户机socket
clientsocket.connect(ip_port)   #连接到服务器

while 1: #循环以接收用户输入，并发送到服务器，接收服务器的回送数据
    data = input('>')   #接收用户输入
    clientsocket.send(data.encode()) #把数据转换为byte对象，并发送到服务器
    if not data:
    	break  #客户端如果退出，服务端收到空消息，退出
    newdata = clientsocket.recv(1024)  #接收服务器的回送数据
    print('Recieve from servr"',repr(newdata)) #输出接收到的数据
    
clientsocket.close()  #关闭客户机
