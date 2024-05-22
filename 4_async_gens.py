import socket
from select import select

tasks = []

to_read = {}
to_write = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_hostname = socket.gethostname()
    server_local_ip = socket.gethostbyname(server_hostname)
    #server_socket.bind(('127.0.0.1', 5000))
    server_socket.bind((server_local_ip, 5000))
    server_socket.listen()
    print(f'Server local ip: {server_local_ip}')

    while True:
        yield ('read', server_socket)
        client_socket, addr = server_socket.accept() # read
        print('Connection from', addr)
        tasks.append(client(client_socket))

def client(client_socket):
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096) # read
        if not request:
            break
        else:
            response = 'Hello world\n'.encode('utf-8') # write
            yield ('write', client_socket)
            client_socket.send(response)

    client_socket.close()

def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)
            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Done!')



if __name__ == '__main__':
    tasks.append(server())
    event_loop()