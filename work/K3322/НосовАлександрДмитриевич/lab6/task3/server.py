import socket

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Request received:\n{request.decode('utf-8')}")

    try:
        with open("index.html", "r") as file:
            html_content = file.read()
    except FileNotFoundError:
        html_content = "<html><body><h1>Error: index.html not found</h1></body></html>"

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n\r\n"
        + html_content
    )

    client_socket.sendall(response.encode('utf-8'))

    client_socket.close()

def start_server(host='127.0.0.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        handle_client(client_socket)

if __name__ == "__main__":
    start_server()

