from socket import *
def main():
    tcp_socket = socket(AF_INET,SOCK_STREAM)  #创建TCP套接字

    tcp_socket.connect(("192.168.31.51",7890))  #链接服务器

    send_data = input("请输入要发送的数据")
    tcp_socket.send(send_data.encode("utf-8"))  #发送数据


    tcp_socket.close()

if __name__ == "__main__":
    main()