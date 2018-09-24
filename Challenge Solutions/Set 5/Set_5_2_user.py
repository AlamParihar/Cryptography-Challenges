import socket
import time
import random
import os
import set_4_4 as s4_4
import set_2_2 as s2_2

class Client():
    def __init__(self):
        self.client=socket.socket()

    def connectTo(self, port, host=socket.gethostname()):
        self.client.connect((host, port))

    def send(self, message):
        self.client.send(message)
        return

    def recieve(self):
        incoming=self.client.recv(1024)
        return incoming

    def close(self):
        self.client.close()

def main():
    print("Running Client")
    p=37
    g=5
    a=random.randint(0, p)
    A=pow(g, a, p)
    client1=Client()

    print("*Client* | Attempting Connection")
    client1.connectTo(3500, socket.gethostname())
    status=client1.recieve()
    print(str(status))

    client1.send(p.to_bytes(16, 'big'))
    client1.send(g.to_bytes(16, 'big'))
    client1.send(A.to_bytes(16, 'big'))

    B=client1.recieve()
    B=int.from_bytes(B, 'big')
    s=pow(B, a, p)


    message=b"Shh. Issa Secret."
    SHA=s4_4.SHA1()
    CBCkey=bytes.fromhex(SHA.Hash(bytes([s]))[0:32])
    IV=os.urandom(16)
    encrypted_message=s2_2.CBC_encrypt(message, CBCkey, IV)

    client1.send(encrypted_message)
    client1.send(IV)

    bot_message=client1.recieve()
    bot_IV=client1.recieve()


    returned_message=s2_2.CBC_decrypt(bot_message, CBCkey, bot_IV)
    print("*CLIENT* | Echoed Message: " + str(returned_message))
    client1.close()
