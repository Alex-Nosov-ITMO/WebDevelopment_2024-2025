import socket

HOST = 'localhost'
PORT = 65432

# Ввод значений с клавиатуры
a = input("Введите катет a: ")
b = input("Введите катет b: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = f"{a} {b}"
    s.sendall(message.encode())
    data = s.recv(1024)

print(f"[CLIENT] Ответ от сервера: {data.decode()}")

