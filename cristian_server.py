import socket
import time

def iniciar_servidor():
    host = 'localhost'
    port = 9001
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"Servidor de Tempo (Cristian) rodando na porta {port}...")

    while True:
        conn, addr = s.accept()
        conn.recv(1024) 
        
        tempo_servidor = int(time.time() * 1000)
        
        conn.send(str(tempo_servidor).encode())
        conn.close()

if __name__ == '__main__':
    iniciar_servidor()