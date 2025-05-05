import socket
import threading

# Список клиентов
clients = []

# Список имен пользователей
usernames = {}

def broadcast(message, client_socket, username):
    """Отправить сообщение всем клиентам, кроме отправителя"""
    for client in clients:
        if client != client_socket:
            try:
                # Добавление имени пользователя в сообщение
                formatted_message = f"{username}: {message.decode('utf-8')}\n"
                client.send(formatted_message.encode('utf-8'))
            except:
                # Удалить клиента из списка, если он отключился
                clients.remove(client)

def handle_client(client_socket):
    """Обработчик сообщений от клиента"""
    try:
        # Получаем имя пользователя
        client_socket.send("Enter your username: ".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')
        usernames[client_socket] = username
        
        welcome_message = f"{username} has joined the chat!\n".encode('utf-8')
        broadcast(welcome_message, client_socket, username)

        while True:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket, username)
            else:
                # Если клиент отключился
                print(f"{username} has left the chat.")
                clients.remove(client_socket)
                client_socket.close()
                break
    except:
        clients.remove(client_socket)
        client_socket.close()

def start_server(host='127.0.0.1', port=8080):
    """Запуск сервера"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"Server started on {host}:{port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Добавляем клиента в список
        clients.append(client_socket)
        
        # Запускаем отдельный поток для каждого клиента
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
