from socket import *
def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)#创建套接字

    udp_socket.bind(("",8080))


    while True:

        data = input("请输入要发送的内容：")
        if data == "exit":
            break

    udp_socket.sendto(data.encode("utf-8"),("192.168.31.51",8081))


    udp_socket.close()

if __name__ == "__main__":
    main()