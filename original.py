import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
server_hostname = socket.gethostname()
server_local_ip = socket.gethostbyname(server_hostname)
#server_socket.bind(('127.0.0.1', 5000))
server_socket.bind((server_local_ip, 5000))
server_socket.listen()
print(f'Server local ip: {server_local_ip}')

def accept_connetion(server_socket):
    while True:
        print('Before accept()')
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        send_message(client_socket)

def send_message(client_socket):
    while True:
        print('Before recv()')
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = 'Hello world\n'.encode('utf-8')
            client_socket.send(response)

    client_socket.close()

if __name__ == '__main__':
    accept_connetion(server_socket)