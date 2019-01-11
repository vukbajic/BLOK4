import socket
import re

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8080))

    addr = socket.gethostbyname(socket.gethostname())   #vraca ip adresu racunara
    port = "502"                                        #port za konekciju

    files_for_send = addr + "+" + port

    my_str_as_bytes = str.encode(files_for_send)
    type(my_str_as_bytes) # ensure it is byte representation
    s.sendall(my_str_as_bytes)

    data = s.recv(1024)
    s.close()
    my_decoded_str = data.decode()
    type(my_decoded_str)


    pom = my_decoded_str.split("+")
    print("Adresa " + pom[0])
    print("Port " + pom[1])
    enemySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    enemySocket.connect((pom[0],int(pom[1])))

    print ('Received', repr(my_decoded_str))
    return enemySocket



addr = socket.gethostbyname(socket.gethostname())
line = re.sub('[.]', '', addr)
line = int(line)
print(line)

