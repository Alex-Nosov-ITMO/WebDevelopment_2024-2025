import socket
import math

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Ожидаем подключение на {HOST}:{PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Подключен клиент: {addr}")
        data = conn.recv(1024).decode()
        print(f"[SERVER] Получены данные: {data}")
        
        # разбираем стороны a и b
        try:
            a_str, b_str = data.strip().split()
            a = float(a_str)
            b = float(b_str)
            c = math.sqrt(a ** 2 + b ** 2)
            response = f"Гипотенуза c = {c:.2f}"
        except Exception as e:
            response = f"Ошибка обработки данных: {e}"
        
        conn.sendall(response.encode())
