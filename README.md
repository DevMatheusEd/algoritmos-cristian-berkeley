# Sincronizacao de Relogios em Sistemas Distribuidos

Implementacao em Python de algoritmos de sincronizacao de relogios para ambientes distribuidos, utilizando sockets TCP e operando com precisao em nivel de milissegundos.

## O que foi feito

O projeto contem duas implementacoes principais de sincronizacao temporal baseadas em arquitetura cliente-servidor e coordenador-lider:

1. **Algoritmo de Cristian (Cliente-Servidor)**:
   - Um servidor de tempo responde a requisicoes enviando seu timestamp atual.
   - O cliente calcula o RTT (Round Trip Time) medindo o intervalo entre o envio da requisicao ($T_0$) e o recebimento da resposta ($T_1$).
   - O tempo ajustado do cliente e corrigido considerando metade do RTT somado ao tempo reportado pelo servidor.

2. **Algoritmo de Berkeley (Master-Slave)**:
   - Implementado para um cenario com 5 nós slaves e 1 coordenador (Master).
   - O coordenador recolhe os tempos de todos os nos conectados (simulando variacoes iniciais de desvio de relogio).
   - Calcula-se a media aritmetica dos tempos da rede e o coordenador envia um offset (desvio) individual para cada escravo ajustar o seu relogio de forma sincronizada.

## Estrutura do Repositorio

- `cristian_server.py`: Servidor de tempo para o Algoritmo de Cristian.
- `cristian_client.py`: Cliente que consome o tempo do servidor e calcula o RTT.
- `berkeley_master.py`: Coordenador que gerencia a conexao de 5 nos, calcula a media e distribui os offsets.
- `berkeley_slave.py`: Nos escravos que simulam relogios dessincronizados e aplicam o ajuste recebido.
