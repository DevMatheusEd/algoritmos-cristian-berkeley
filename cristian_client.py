import socket
import time

def sincronizar_relogio():
    host = 'localhost'
    port = 9001
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    t0 = int(time.time() * 1000)
    s.send(b"REQUISICAO_DE_TEMPO")
    
    resposta = s.recv(1024).decode()
    tempo_servidor = int(resposta)
    
    t1 = int(time.time() * 1000)
    
    s.close()
    
    rtt = t1 - t0
    tempo_sincronizado = tempo_servidor + (rtt // 2)
    
    print(f"Tempo local antes da sincronização: {t1} ms")
    print(f"Tempo reportado pelo servidor:      {tempo_servidor} ms")
    print(f"RTT calculado da mensagem:          {rtt} ms")
    print(f"Novo Tempo Sincronizado do Cliente: {tempo_sincronizado} ms")
    print(f"Ajuste aplicado ao relógio:         {tempo_sincronizado - t1} ms")

if __name__ == '__main__':
    sincronizar_relogio()