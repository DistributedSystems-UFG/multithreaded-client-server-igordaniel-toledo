from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    msg = input("Digite operação (ex: add 10 5) ou 'sair': ")

    if msg.lower() == "sair":
        break

    s.send(msg.encode())

    data = s.recv(1024)
    print("Resposta do servidor:", data.decode())

s.close()
