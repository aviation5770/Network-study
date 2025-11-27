from socket import *

serverS = socket(AF_INET, SOCK_STREAM)

serverS.bind(('', 8989))
serverS.listen(1)

print("*이해원* 서버 오픈")

connectionS, addr = serverS.accept()

print("*클라이언트 " + str(addr) + "* 에서 접속 완료")

clntdata = connectionS.recv(1024).decode('utf-8')
print("클라이언트:", clntdata)

msg = input()

connectionS.send(msg.encode('utf-8'))
print("메시지 전송 완료")