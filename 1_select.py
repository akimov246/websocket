import socket
from select import select

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
server_hostname = socket.gethostname()
server_local_ip = socket.gethostbyname(server_hostname)
#server_socket.bind(('127.0.0.1', 5000))
server_socket.bind((server_local_ip, 5000))
server_socket.listen()
print(f'Server local ip: {server_local_ip}')

def accept_connetion(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    to_monitor.append(client_socket)

def send_message(client_socket):
    try:
        request = client_socket.recv(4096)
        print(request)

        if request:
            response = 'Hello world\n'.encode('utf-8')
            client_socket.send(response)
        else:
            client_socket.close()
            to_monitor.remove(client_socket)
    except ConnectionResetError:
        client_socket.close()
        to_monitor.remove(client_socket)
        print(f'Client disconnected')

def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], []) # read, write, errors

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connetion(sock)
            else:
                send_message(sock)

if __name__ == '__main__':
    to_monitor.append(server_socket)
    #accept_connetion(server_socket)
    event_loop()