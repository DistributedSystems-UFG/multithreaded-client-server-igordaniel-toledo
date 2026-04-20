from socket import *
from constCS import *
import threading
import random
import time

NUM_REQUISICOES = 100  # pode aumentar

def gerar_operacao():
    op = random.choice(["add", "sub", "mul", "div"])
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    
    if op == "div" and b == 0:
        b = 1
        
    return f"{op} {a} {b}"

def enviar_requisicao(i):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    msg = gerar_operacao()

    inicio = time.time()

    s.send(msg.encode())
    data = s.recv(1024)

    fim = time.time()

    print(f"Req {i}: {msg} = {data.decode()} | Tempo: {fim - inicio:.5f}s")

    s.close()


threads = []
inicio_total = time.time()

for i in range(NUM_REQUISICOES):
    t = threading.Thread(target=enviar_requisicao, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

fim_total = time.time()

print("\nTempo total:", fim_total - inicio_total)
