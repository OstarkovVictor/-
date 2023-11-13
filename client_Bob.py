from tkinter import *
import pyaudio
import socket
from threading import Thread
FORMAT = pyaudio.paInt16
import time
CHANNELS = 1
RATE = 10000
CHUNK = 1000
client_socket_text = socket.socket()
client_socket_text.connect(("127.0.0.1", 6000))
client_socket_voice = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
audio = pyaudio.PyAudio()

def connect_voice():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5000))
    return client_socket
def send_voice(in_data, frame_count, time_info, status):
    while True:
            client_socket_voice.send(in_data)
            return (None, pyaudio.paContinue)
def recive_voice():
    while True:
        try:
            a = client_socket_voice.recv(1000)
            streamout.write(a)
        except:pass
tread1 = Thread(target=recive_voice, daemon=True)
tread1.start()

def sender():
  while True:
      time.sleep(2)



      client_socket_text.send("--".encode("utf-8"))
def recive_text():
    while True:
        time.sleep(0.005)
        b = client_socket_text.recv(2048)
        # if not ("--" in b.decode("utf-8")):
        b_mess = b.decode("utf-8").replace("-","")

        if b_mess != "":

            lbl_text.insert("0.1", "\n" + b_mess)
tread2 = Thread(target=sender)
tread3 = Thread(target=recive_text, daemon=True)
tread2.start()
tread3.start()

print(1)
def clicked_voice():
    global audio
    audio = pyaudio.PyAudio()
    global streamin
    streamin = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=send_voice)
    global streamout
    streamout = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
    global client_socket_voice
    try:
        client_socket_voice = connect_voice()
    except EXCEPTION as e:print(e,1)
    btn.configure(command=clicked_voice_off)
    btn.configure(text="Подключение")
    btn.configure(text="Отключиться")
    return client_socket_voice
def clicked_voice_off():
    global streamin
    streamin.close()
    global streamout
    streamout.close()
    global client_socket_voice
    tread1.join(2)
    btn.configure(text="Подключиться")
    btn.configure(command = clicked_voice)
    client_socket_voice.shutdown(socket.SHUT_RDWR)
    client_socket_voice.close()
    print('off')
def clicked_text():
    global client_socket_text
    a = entry.get()
    client_socket_text.send(("\nBob:: "+a).encode("utf-8"))
    lbl_text.insert("0.1", "\nYou:: " + a)
    lbl_text.pack(ipady = 8)





    entry.delete(0,'end')

window = Tk()
window.title("Bob's window")
window.geometry('600x900')
btn = Button(window, text="Подключиться к серверу голосовой связи", command=clicked_voice)
btn.pack(side=TOP)
lbl_text = Text(window, font=("Arial Bold", 18))
lbl_text.insert("0.1","\nserver connected")
rolled_view = Scrollbar(window,orient='vertical', command=lbl_text.yview)
entry = Entry()
entry.pack( side = TOP)
btn_text = Button(window, text="Отправить", command=clicked_text)
btn_text.pack(side=TOP)
lbl_text.pack(ipady = 8)
while True:
    window.mainloop()