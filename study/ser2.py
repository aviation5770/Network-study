from socket import *
import threading
import time

def s(sck):
    while True:
        t = input()
        sck.send(t.encode('utf-8'))

def r(sck, name):
    while True:
        t = sck.recv(1024).decode('utf-8')
        print(name, ">>", t)

srv = socket(AF_INET, SOCK_STREAM)
# AF_INET: IPv4
# SOCK_STREAM: TCP

srv.bind(('', 8990))
srv.listen(1)

print("*서버 오픈*")

conn, adr = srv.accept()

print("*클라이언트", adr, "접속*")

name = conn.recv(1024).decode('utf-8')

ts = threading.Thread(target=s, args=(conn,))
tr = threading.Thread(target=r, args=(conn, name))

ts.start()
tr.start()

while True:
    time.sleep(1)
    pass