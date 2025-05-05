import socket

HOST = 'localhost'  # 127.0.0.1
PORT = 65432        # любой свободный порт > 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Ждём подключения на {HOST}:{PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Подключен клиент: {addr}")
        data = conn.recv(1024)
        print(f"[SERVER] Получено сообщение: {data.decode()}")
        conn.sendall(b"Hello, client")
