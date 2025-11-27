from socket import *

clientS = socket(AF_INET, SOCK_STREAM)

clientS.connect(('127.0.0.1', 8989))

print("*이해원* 서버 연결됨")

msg = input()
clientS.send(msg.encode('utf-8'))

print("메시지 전송 완료")

servdata = clientS.recv(1024).decode('utf-8')
print(servdata, "가 성공적으로 수신되었습니다.")