import socket

def handle_client(client_socket):
    try:
        request = client_socket.recv(1024)

        # Безопасное декодирование
        request_str = request.decode('utf-8', errors='replace')
        print(f"Request received:\n{request_str}")

        request_lines = request_str.split('\r\n')
        request_line = request_lines[0] if request_lines else ''

        if not request_line or len(request_line.split()) < 2:
            print("Invalid request line, closing connection.")
            return

        method, path, *_ = request_line.split()

        if path == "/favicon.ico":
            response = (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n\r\n"
                "<html><body><h1>404 Favicon Not Found</h1></body></html>"
            )
        elif path != "/":
            response = (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n\r\n"
                "<html><body><h1>404 Page Not Found</h1></body></html>"
            )
        else:
            try:
                with open("index.html", "r", encoding="utf-8") as file:
                    html_content = file.read()
            except FileNotFoundError:
                html_content = "<html><body><h1>Error: index.html not found</h1></body></html>"

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "Connection: close\r\n\r\n"
                + html_content
            )

        client_socket.sendall(response.encode('utf-8'))

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
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

