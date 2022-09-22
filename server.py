import socket
import threading

host_n = '127.0.0.1' 
port = 7976 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# host_name = socket.gethostname()        
# s_ip = socket.gethostbyname(host_name)   

server.bind((host_n, port))  
server.listen()


clients = []
nicknames = []


def broadcast(message):  
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try: 
            message = client.recv(1024)
            broadcast(message)
        except: 
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():  
    while True:
        client, address = server.accept()
        # client = server.accept()
        print("Connected with {}".format(str(address)))
        client.send('NICKNAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print("Username {}".format(nickname))
        broadcast("{} connected!".format(nickname).encode('utf-8'))
        client.send('Connected to Server'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()