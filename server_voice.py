import socket
from threading import Thread
socket_voice = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_voice.bind(('127.0.0.1', 5000))


socket_voice.listen(2)
print("Server is up now!")
conn1, add1 = socket_voice.accept()
conn2, add2 = socket_voice.accept()
clients = [conn1,conn2]


def route():
    global clients


    while True:
        try:

            for client_sender in clients:
                voice = client_sender.recv(1000)
                for i in clients:
                    if i == client_sender:
                        pass
                    else:i.send(voice)


        except:
            conn1, add1 = socket_voice.accept()
            conn2, add2 = socket_voice.accept()
            clients = [conn1, conn2]



tread1 = Thread(target=route(), daemon=True)
tread1.start()
