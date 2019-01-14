MAIN_SERVER_ADDR = '192.168.1.8'
import select, socket,queue
from multiprocessing import Queue
from multiprocessing import Process
import  time



class Client:
    def __init__(self):
        self.addr = ""
        self.port = -1
        self.socket = None
        self.num = -1


def inputProcess(que,que2,server,inputs,outputs,message_queues):
    client_count = 0
    clients = []
    winners = []
    winner_count = 0
    while inputs:
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs)
        for s in readable:
            if s is server:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                message_queues[connection] = queue.Queue()
            else:
                data = s.recv(1024)
                c1 = Client()

                my_decoded_str = data.decode()
                type(my_decoded_str)


                if(len(my_decoded_str) > 0):
                    pom = my_decoded_str.split("+")

                    temp = s.getpeername()
                    addr = temp[0]

                    print(len(pom))
                    if len(pom) > 1:
                        c1.addr = addr
                        c1.port = int(pom[1])
                        c1.socket = s
                        if pom[0] == "Winner":
                            winner_count += 1
                            c1.num = winner_count
                            winners.append(c1)
                        else:
                            client_count += 1
                            c1.num = client_count
                            clients.append(c1)

                    for client in clients:
                        print("Klient " + str(client.num))
                        print("addr: " + client.addr)
                        print("port: " + str(client.port))
                        print("socket" + str(client.socket))

                    for client in winners:
                        print("Winner " + str(client.num))
                        print("addr: " + client.addr)
                        print("port: " + str(client.port))
                        print("socket" + str(client.socket))

                que.put([clients,client_count,pom[0]])
                que2.put([winners,winner_count,pom[0]])


def gameProces(que):

    client_count = 0
    clients, client_count, msg = que.get()
    print("msg" + msg)
    if msg == 'Online_game':
        while client_count != 2:
            clients, client_count, msg = que.get()
        c1 = clients[0]
        c2 = clients[1]

        files_for_send = c2.addr + "+" + str(c2.port)
        my_str_as_bytes = str.encode(files_for_send)
        type(my_str_as_bytes)  # ensure it is byte representation
        c1.socket.send(my_str_as_bytes)

        files_for_send = c1.addr + "+" + str(c1.port)
        my_str_as_bytes = str.encode(files_for_send)
        type(my_str_as_bytes)  # ensure it is byte representation
        c2.socket.send(my_str_as_bytes)

    elif msg == "tournament":
        while client_count != 4:
            clients, client_count, msg = que.get()

        c1 = clients[0]
        c2 = clients[1]
        c3 = clients[2]
        c4 = clients[3]

        files_for_send = c2.addr + "+" + str(c2.port)
        my_str_as_bytes = str.encode(files_for_send)
        type(my_str_as_bytes)  # ensure it is byte representation
        c1.socket.send(my_str_as_bytes)

        files_for_send = c1.addr + "+" + str(c1.port)
        my_str_as_bytes = str.encode(files_for_send)
        type(my_str_as_bytes)  # ensure it is byte representation
        c2.socket.send(my_str_as_bytes)

        files_for_send = c4.addr + "+" + str(c4.port)
        my_str_as_bytes = str.encode(files_for_send)
        type(my_str_as_bytes)  # ensure it is byte representation
        c3.socket.send(my_str_as_bytes)

        files_for_send = c3.addr + "+" + str(c3.port)
        my_str_as_bytes = str.encode(files_for_send)
        type(my_str_as_bytes)  # ensure it is byte representation
        c4.socket.send(my_str_as_bytes)



def winnerAction(que):

    winners,winner_count,msg = que.get()

    while len(winners) != 2:
        winners, winner_count,msg = que.get()


    c1 = winners[0]
    c2 = winners[1]

    files_for_send = c2.addr + "+" + str(c2.port)
    my_str_as_bytes = str.encode(files_for_send)
    type(my_str_as_bytes)  # ensure it is byte representation
    c1.socket.send(my_str_as_bytes)

    files_for_send = c1.addr + "+" + str(c1.port)
    my_str_as_bytes = str.encode(files_for_send)
    type(my_str_as_bytes)  # ensure it is byte representation
    c2.socket.send(my_str_as_bytes)




if __name__ == '__main__':
    que = Queue()
    que2 = Queue()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    server.bind(("", 8080))
    server.listen(5)
    inputs = [server]
    outputs = []
    message_queues = {}

    clients = []


    p1 = Process(target=gameProces, args=(que,))
    p1.start()

    p3 = Process(target=winnerAction, args=(que2,))
    p3.start()

    p2 = Process(target=inputProcess, args=(que,que2,server,inputs,outputs,message_queues,))
    p2.start()


