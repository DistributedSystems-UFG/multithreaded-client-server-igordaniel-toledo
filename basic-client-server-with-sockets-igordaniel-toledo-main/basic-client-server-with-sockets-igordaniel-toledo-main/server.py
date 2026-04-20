from socket import *
from constCS import *
import threading

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

# ✅ função para cada cliente (thread)
def atender_cliente(conn, addr):
    print("Conectado por:", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break

        mensagem = data.decode()
        print(f"[{addr}] Recebido:", mensagem)

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
    print("Desconectado:", addr)


# socket principal
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print("Servidor aguardando conexões...")

while True:
    conn, addr = s.accept()

    # ✅ nova thread por cliente
    t = threading.Thread(target=atender_cliente, args=(conn, addr))
    t.start()
