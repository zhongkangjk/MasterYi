from socket import *
def main():
    tcp_server_socket = socket(AF_INET,SOCK_STREAM)  #创建套接字

    tcp_server_socket.bind(("",7890))  #绑定本地信息

    tcp_server_socket.listen(128)  #设置为监听模式

    while True:
        print("等待一个新的客户端到来")
        #等别人发信息来
        new_client_socket,client_addr = tcp_server_socket.accept()
        print("他来了")
        recv_data = new_client_socket.recv(1024)#接收
        print("他发送的是：%s" % recv_data.decode("utf-8"))

        new_client_socket.send("ahhahaha------ok----".encode("utf-8"))
        #给他回一个

        new_client_socket.close()
        print("已经服务完毕")




if __name__ == "__main__":
    main()