import socket
import selectors

selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_hostname = socket.gethostname()
    server_local_ip = socket.gethostbyname(server_hostname)
    #server_socket.bind(('127.0.0.1', 5000))
    server_socket.bind((server_local_ip, 5000))
    server_socket.listen()
    print(f'Server local ip: {server_local_ip}')

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connetion)

def accept_connetion(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)

def send_message(client_socket):
    try:
        request = client_socket.recv(4096)
        print(request)

        if request:
            response = 'Hello world\n'.encode('utf-8')
            client_socket.send(response)
        else:
            selector.unregister(fileobj=client_socket)
            client_socket.close()
    except ConnectionResetError:
        selector.unregister(fileobj=client_socket)
        client_socket.close()
        print(f'Client disconnected')

def event_loop():
    while True:
        events = selector.select() # (key, events)
        # SelectorKey
        #fileobj
        #events
        #data
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == '__main__':
    #accept_connetion(server_socket)
    server()
    event_loop()