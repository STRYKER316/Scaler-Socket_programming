import socket


# 1> create a socket object
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = '127.0.0.1'
server_port = 8089
# 2> connect socket object to server host and its port
client_sock.connect((server_host, server_port))         # 3-way handshake here

# 3> send request to the server from client
request_data = 'Hello from the client sides'
client_sock.sendall(request_data.encode())

# 4> Client receives response from server
response_data = client_sock.recv(1024).decode()
print('Data received from server: ' + response_data)

# 5> close the socket
client_sock.close()
