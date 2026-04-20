# Sistema Cliente-Servidor com Multithreading

## Visão Geral

Este projeto implementa um sistema cliente-servidor utilizando sockets TCP em Python para processamento de operações matemáticas.

O objetivo é comparar o desempenho entre diferentes abordagens de concorrência:

- Execução sequencial (single-thread)
- Multithreading apenas no servidor
- Multithreading no cliente e no servidor

---

## Funcionalidades

O cliente envia operações no formato:
operacao num1 num2


Exemplos:


add 10 5
sub 8 3
mul 4 6
div 10 2


O servidor processa a requisição e retorna o resultado correspondente.

---

## Arquitetura

### Versão 1 — Single-thread

- Cliente envia requisições sequencialmente
- Servidor atende apenas uma conexão por vez

### Versão 2 — Multithread no Servidor

- Servidor cria uma thread para cada cliente
- Cliente continua sequencial

### Versão 3 — Multithread Cliente + Servidor

- Cliente cria uma thread para cada requisição
- Servidor cria uma thread para cada conexão

---

## Geração de Requisições

Na versão multithread, o cliente gera automaticamente:

- Operações: `add`, `sub`, `mul`, `div`
- Números aleatórios entre 1 e 100

---

## Medição de Desempenho

O tempo total de execução é medido no cliente utilizando:

```python
time.time()

Resultados (exemplo)
| Versão                         | Tempo (100 requisições) |
| ------------------------------ | ----------------------- |
| Single-thread                  | 5.23 s                  |
| Multithread no servidor        | 2.11 s                  |
| Cliente + servidor multithread | 0.89 s                  |
