Sistema Cliente-Servidor com Multithreading
Descrição

Este projeto implementa um sistema cliente-servidor utilizando sockets TCP em Python, com o objetivo de processar operações matemáticas enviadas pelo cliente.

O sistema foi desenvolvido em três versões para análise de desempenho:

Single-thread (execução sequencial)
Multithreading apenas no servidor
Multithreading no cliente e no servidor
Funcionalidades

O cliente envia operações no seguinte formato:

operacao num1 num2

Exemplos:

add 10 5
sub 8 3
mul 4 6
div 10 2

O servidor processa a operação e retorna o resultado ao cliente.

Implementações
1. Versão Single-thread
O cliente envia requisições de forma sequencial
O servidor atende apenas um cliente por vez

Essa abordagem é simples, porém apresenta baixo desempenho com muitas requisições.

2. Multithreading no Servidor
O servidor cria uma thread para cada cliente conectado
O cliente continua enviando requisições de forma sequencial

Essa abordagem permite o atendimento simultâneo de múltiplos clientes.

3. Multithreading no Cliente e no Servidor
O cliente cria uma thread para cada requisição enviada
O servidor cria uma thread para cada conexão recebida

Essa abordagem maximiza o paralelismo e apresenta o melhor desempenho.

Geração Automática de Requisições

Na versão multithread do cliente, as requisições são geradas automaticamente utilizando números aleatórios:

Operações: add, sub, mul, div
Valores entre 1 e 100
Medição de Desempenho

O tempo total de execução é medido no cliente utilizando a função:

time.time()
Resultados (exemplo)

Quantidade de requisições: 100

Single-thread: 5.23 s
Multithreading apenas no servidor: 2.11 s
Multithreading no cliente e servidor: 0.89 s
Análise

A versão single-thread apresentou maior tempo de execução devido ao processamento sequencial das requisições.

A versão com multithreading no servidor apresentou melhora no desempenho ao permitir o atendimento simultâneo de múltiplos clientes.

A versão com multithreading tanto no cliente quanto no servidor apresentou o melhor desempenho, devido ao envio e processamento paralelo das requisições.

Como Executar
1. Configurar o endereço

No arquivo constCS.py:

HOST = '127.0.0.1'
PORT = 5678
2. Executar o servidor
python server_multithread.py
3. Executar o cliente
python client_multithread.py
Estrutura do Projeto
.
├── client_multithread.py
├── server_multithread.py
├── constCS.py
└── README.md
