from socket import *
from constCS import *

def calcular(operacao, a, b):
    if operacao == "add":
        return a + b
    elif operacao == "sub":
        return a - b
    elif operacao == "mul":
        return a * b
    elif operacao == "div":
        if b == 0:
            return "Erro: divisão por zero"
        return a / b
    else:
        return "Erro: operação inválida"

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("Servidor aguardando conexão...")
(conn, addr) = s.accept()
print("Conectado por:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    mensagem = data.decode()
    print("Recebido:", mensagem)

    try:
        partes = mensagem.split()
        operacao = partes[0]
        a = float(partes[1])
        b = float(partes[2])

        resultado = calcular(operacao, a, b)
    except:
        resultado = "Erro no formato. Use: operacao num1 num2"

    conn.send(str.encode(str(resultado)))

conn.close()
