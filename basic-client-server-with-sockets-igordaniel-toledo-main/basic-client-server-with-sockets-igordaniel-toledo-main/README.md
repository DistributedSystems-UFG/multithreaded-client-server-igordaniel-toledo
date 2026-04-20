# Sistema Cliente-Servidor: Calculadora Distribuída

## Descrição

Este projeto implementa um sistema distribuído simples utilizando sockets TCP em Python. O sistema consiste em um cliente e um servidor, onde o servidor realiza operações matemáticas solicitadas remotamente pelo cliente.

## Funcionalidades

O servidor oferece as seguintes operações:

* Soma (`add`)
* Subtração (`sub`)
* Multiplicação (`mul`)
* Divisão (`div`)

O cliente envia uma requisição contendo a operação desejada e dois valores numéricos. O servidor processa os dados e retorna o resultado.

## Formato das mensagens

O cliente deve enviar mensagens no seguinte formato:

operacao valor1 valor2[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)
Starter code for the basic client-server assignment


Este template corresponde ao exemplo da Fig. 2.3 do livro. O exercício consiste em acrescentar funcionalidade ao servidor para torná-lo mais útil. Essa funcionalidade deve ser acessível aos clientes. Por exemplo, o servidor pode ser uma espécie de calculadora remota. O cliente passa dois valores numéricos, juntamente com o nome de uma operação (ex.: add, subtract, multiply, divide) e o servidor executa a operação respectiva e retorna seu resultado para o cliente. Você pode implementar um servidor com outras funcionalidades (diferente da calculadora). O imporante é que ele ofereça pelo menos três operações diferentes que os clientes podem utilizar remotamente, passando dados para serem processados e recebendo o resultado desse processamento como resposta.

Tarefa individual.

Incluir um Readme descritivo do sistema implementado.

Exemplo:
add 10 5

## Execução

1. Inicie o servidor:
   python server.py

2. Em outro terminal, execute o cliente:
   python client.py

3. Digite as operações no cliente.

## Tratamento de erros

* Operações inválidas são tratadas pelo servidor.
* Divisão por zero retorna mensagem de erro.
* Formatos incorretos também são tratados.

## Tecnologias utilizadas

* Python
* Sockets TCP

## Observações

O sistema suporta comunicação contínua até que o cliente digite "sair".

