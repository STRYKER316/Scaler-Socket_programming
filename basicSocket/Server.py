import socket

# ------------ Boot up the server -----------
# 1> create socket object
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = '127.0.0.1'
server_port = 8089
# 2> bind the socket to the host and port
server_sock.bind((server_host, server_port))

# 3> start listening for client connections
server_sock.listen()
print("Server Boot-up is complete")

# ------------- start accepting client requests -----------
# 4> Accept a client connection
connection, address = server_sock.accept()  # 3-way handshake
print("Received connection request from a client")

# 5> Receive the client request
request_data = connection.recv(1024).decode()

# 6> process the request
print('Data received from client: ' + request_data)

# 7> send a response back to the client
connection.sendall('Hey from the server side'.encode())

# 8> close the connection
connection.close()

# 9> terminate the server
server_sock.close()
