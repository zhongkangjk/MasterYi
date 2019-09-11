import time
import threading

def helloworld():
    for i in range(5):
        print("----helloworld----")
        time.sleep(1)

def hellohome():
    """跳舞5秒钟"""
    for i in range(5):
        print("----hellohome----")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=helloworld)  #如果要传参数可加args = （元组）
    t2 = threading.Thread(target=hellohome)
    t1.start()
    t2.start()
if __name__ == "__main__":
    main()


