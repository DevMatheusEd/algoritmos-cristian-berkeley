import socket
import time

def coordenador_berkeley(num_nos=5):
    host = 'localhost'
    port = 9000
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(num_nos)
    
    conexoes = []
    print(f"Aguardando {num_nos} nós se conectarem para sincronização Berkeley...")
    
    for _ in range(num_nos):
        conn, addr = s.accept()
        conexoes.append((conn, addr))
        print(f"Nó conectado: {addr}")
        
    tempos_nos = []
    
    tempo_mestre = int(time.time() * 1000)
    tempos_nos.append(tempo_mestre)
    print(f"\nTempo do Mestre: {tempo_mestre} ms")


    for conn, addr in conexoes:
        conn.send(b"ENVIE_SEU_TEMPO")
        tempo_escravo = int(conn.recv(1024).decode())
        tempos_nos.append(tempo_escravo)
        print(f"Tempo recebido do Nó {addr}: {tempo_escravo} ms")
        

    tempo_medio = sum(tempos_nos) // len(tempos_nos)
    print(f"\n[!] Tempo Médio Calculado: {tempo_medio} ms")
    print(f"[!] Ajuste no próprio Mestre: {tempo_medio - tempo_mestre} ms")
    

    for i, (conn, addr) in enumerate(conexoes):
        # i + 1 porque o índice 0 é o Mestre na lista tempos_nos
        tempo_escravo_original = tempos_nos[i + 1] 
        offset = tempo_medio - tempo_escravo_original
        conn.send(str(offset).encode())
        conn.close()
        print(f"Enviado offset de {offset} ms para o Nó {addr}")

if __name__ == '__main__':
    coordenador_berkeley(num_nos=5)