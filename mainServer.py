import select, socket, sys, queue
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(("0.0.0.0", 8080))
server.listen(5)
inputs = [server]
outputs = []
message_queues = {}

clients = []

client_count = 1

class Client:
    def __init__(self):
        self.addr = ""
        self.port = -1
        self.socket = None
        self.num = -1

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
            print("Primljeno: " + my_decoded_str )

            if(len(my_decoded_str) > 0):
                pom = my_decoded_str.split("+")

                print(len(pom))
                if len(pom) > 1:
                    c1.addr = pom[0]
                    c1.port = int(pom[1])
                    c1.num = client_count
                    c1.socket = s
                    client_count += 1
                    clients.append(c1)

                for client in clients:
                    print("Klient " + str(client.num))
                    print("addr: " + client.addr)
                    print("port: " + str(client.port))
                    print("socket" + str(client.socket))

            if client_count == 3:
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




