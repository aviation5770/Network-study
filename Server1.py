from socket import *

serverS = socket(AF_INET, SOCK_STREAM)

serverS.bind(('0.0.0.0', 8989))
serverS.listen(1)

print('*이해원* 서버 오픈')

connectionS, addr = serverS.accept()
print(str(addr), '에서 접속 완료')

clntdata = connectionS.recv(2007)
print('클라이언트:', clntdata.decode('utf-8'))

msg = input()
connectionS.send(msg.encode('utf-8'))
print('메시지 전송 완료')