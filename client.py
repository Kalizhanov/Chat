import socket
import threading

nickname = input("Выберите имя пользователя: ")
id = int(input("Your id: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

client.connect(('127.0.0.1', 8080))  
# socket_server = socket.socket()
# server_host = socket.gethostname()
# ip = socket.gethostbyname(server_host)

# socket_server.connect((server_host, 7976))

def rec():
    while True: 
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)

        except:  
            print("ERror!")
            client.close()
            break

def wr():
    while True: 
        message = '{}: {}'.format(nickname, input('me: '))
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=rec) 
receive_thread.start()
write_thread = threading.Thread(target=wr)
write_thread.start()
