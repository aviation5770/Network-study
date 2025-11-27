from socket import *
import threading
import time

def s(sck):
    while True:
        t = input()
        sck.send(t.encode('utf-8'))

def r(sck):
    while True:
        t = sck.recv(1024).decode('utf-8')
        print("서버 >>", t)

cli = socket(AF_INET, SOCK_STREAM)
# AF_INET: IPv4
# SOCK_STREAM: TCP

cli.connect(('127.0.0.1', 8990))

name = input("이름: ")
print(f"*{name}* 연결됨")

cli.send(name.encode('utf-8'))

ts = threading.Thread(target=s, args=(cli,))
tr = threading.Thread(target=r, args=(cli,))

ts.start()
tr.start()

while True:
    time.sleep(1)
    pass