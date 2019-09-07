from socket import *
def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)#创建套接字

    udp_socket.bind(("",8081))


    while True:

        data = input("请输入要发送的内容：")
        if data == "exit":
            break
        else :
            udp_socket.sendto(data.encode("utf-8"), ("192.168.31.51", 8080))




    udp_socket.close()

if __name__ == "__main__":
    main()