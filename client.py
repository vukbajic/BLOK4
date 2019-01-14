import socket
from globals import *
import threading
from queue import Queue


def connect(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((MAIN_SERVER_ADDR, 8080))

    files_for_send = msg + "+" + str(MY_PORT)

    my_str_as_bytes = str.encode(files_for_send)
    type(my_str_as_bytes) # ensure it is byte representation

    t1 = threading.Thread(target=send,args=(s,my_str_as_bytes))
    t1.start()
    t1.join()

    que = Queue()

    t2 = threading.Thread(target=recv, args=(s,que))
    t2.start()
    t2.join()

    data = que.get()

    print("POSLAO")

    s.close()
    my_decoded_str = data.decode()
    type(my_decoded_str)

    pom = my_decoded_str.split("+")
    print("Adresa " + pom[0])
    print("Port " + pom[1])

    print ('Received', repr(my_decoded_str))
    return pom[0],pom[1]

def send(soc,msg):
    soc.sendall(msg)

def recv(soc,que):
    data = soc.recv(1024)
    que.put(data)


