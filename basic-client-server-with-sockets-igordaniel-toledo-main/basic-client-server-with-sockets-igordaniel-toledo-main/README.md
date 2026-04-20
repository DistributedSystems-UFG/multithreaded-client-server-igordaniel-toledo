# Sistema Cliente-Servidor com Multithreading

## Descrição

Este projeto implementa um sistema cliente-servidor utilizando sockets TCP em Python, com o objetivo de processar operações matemáticas enviadas pelo cliente.

O sistema foi desenvolvido em três versões para análise de desempenho:

- Single-thread (execução sequencial)
- Multithreading apenas no servidor
- Multithreading no cliente e no servidor

---

## Funcionalidades

O cliente envia operações no seguinte formato:

operacao num1 num2


Exemplos:


add 10 5
sub 8 3
mul 4 6
div 10 2

O servidor processa a operação e retorna o resultado.

---

## Implementações

### 1. Versão Single-thread

- Cliente envia requisições sequencialmente
- Servidor atende um cliente por vez

---

### 2. Multithreading no Servidor

- Servidor cria uma thread para cada cliente
- Cliente permanece sequencial

---

### 3. Multithreading no Cliente e no Servidor

- Cliente cria uma thread por requisição
- Servidor cria uma thread por conexão

---

## Geração Automática

O cliente multithread gera operações aleatórias:

- Operações: add, sub, mul, div
- Valores entre 1 e 100

---

## Medição de Desempenho

Tempo medido com:

```python
time.time()
