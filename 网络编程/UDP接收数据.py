from socket import *
def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)  #创建套接字
    localaddr = ("",7788)
    udp_socket.bind(localaddr)  #绑定一个本地信息
    while True:
        recv_data = udp_socket.recvfrom(1024)  #接收数据
        recv_msg = recv_data[0]  #消息
        send_addr = recv_data[1]  #地址
        # print(recv_data)
        print("%s:%s" % (str(send_addr),recv_msg.decode("GBK")))

    udp_socket.close()

if __name__ == "__main__":
    main()