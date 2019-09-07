from socket import *
def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)#创建套接字
    #dest_ip = input("对方ip")
    #dest_port = int(input(""))
    data = input("请输入要发送的内容：")
    udp_socket.sendto(data.encode("utf-8"), ("192.168.31.51",8080))

    recv_data = udp_socket.recvfrom(1024)  # 接收数据
    print(recv_data)

    #udp_socket.close()

if __name__ == "__main__":
    main()