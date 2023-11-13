import socket
from threading import Thread
socket_text = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


socket_text.bind(('127.0.0.1', 6000))
socket_text.listen(2)
connection1, add1 = socket_text.accept()
connection2, add2 = socket_text.accept()
clients = [connection1, connection2]





def route():
    global clients
    while True:
        try:
            for client_sender in clients:
                text = client_sender.recv(1024)
                for client_reciver in clients:
                    if client_reciver == client_sender:
                        pass
                    else:client_reciver.send(text)
        except:
            connection1, add1 = socket_text.accept()
            connection2, add2 = socket_text.accept()

            clients = [connection1, connection2]



tread_text = Thread(target=route(), daemon=True)
tread_text.start()