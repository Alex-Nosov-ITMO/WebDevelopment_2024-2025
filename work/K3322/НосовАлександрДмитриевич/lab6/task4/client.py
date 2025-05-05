import socket
import threading

def receive_messages(client_socket):
    """Получать сообщения от сервера и отображать имя пользователя"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)  # Печатаем сообщение с именем отправителя
        except:
            print("Disconnected from server.")
            break

def send_message(client_socket):
    """Отправлять сообщения на сервер"""
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

def start_client(host='127.0.0.1', port=8080):
    """Запуск клиента"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Создаем потоки для получения и отправки сообщений
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client()
