import socket
import time
import random

def slave_knot():
    host = 'localhost'
    port = 9000
    

    erro_simulado_ms = random.randint(-10000, 10000) 
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("Conectado ao Coordenador. Aguardando comando...")
    
    comando = s.recv(1024)
    if comando == b"ENVIE_SEU_TEMPO":
        # Lê o tempo local corrompido propositalmente para teste
        meu_tempo = int(time.time() * 1000) + erro_simulado_ms
        s.send(str(meu_tempo).encode())
        print(f"Meu tempo dessincronizado enviado: {meu_tempo} ms (Erro simulado: {erro_simulado_ms} ms)")
        

        offset = int(s.recv(1024).decode())
        

        novo_tempo = meu_tempo + offset
        print(f"Offset recebido do Coordenador:    {offset} ms")
        print(f"Meu novo tempo sincronizado:       {novo_tempo} ms")
    
    s.close()

if __name__ == '__main__':
    slave_knot()