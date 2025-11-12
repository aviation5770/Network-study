from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(("127.0.0.1", 8081))

print("연결이 확인되었습니다.")
clientSock.send("안녕 나는 클라이언트야".encode('utf-8'))

print("메세지를 전송했습니다.")

data = clientSock.recv(1024)
print("받은 데이터: ", data.decode('utf-8'))