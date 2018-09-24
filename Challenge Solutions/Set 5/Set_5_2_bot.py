import socket
import time
import random
import os
import set_4_4 as s4_4
import set_2_2 as s2_2

from crypto.Hash import SHA1

class Bot():
    def __init__(self, port, host=socket.gethostname()):
        self.bot = socket.socket()
        self.host=host
        self.port=port
        return

    def setAddress(self, port, host=socket.gethostname()):
        self.port=port
        self.host=host
        return

    def bind_bot(self):
        print("Binding Bot")
        self.bot.bind((self.host, self.port))
        return

    def run_bot(self):
        print("Running Bot")
        self.bind_bot()
        self.bot.listen()
        client, addr = self.bot.accept()
        client.send(b"Connected")

        p=client.recv(1024)
        p=int.from_bytes(p, 'big')

        g=client.recv(1024)
        g=int.from_bytes(g, 'big')

        A=client.recv(1024)
        A=int.from_bytes(A, 'big')

        b=random.randint(0, p)

        B=int(pow(g, b, p))

        client.send(B.to_bytes(16, 'big'))
        client_message=client.recv(1024)
        client_IV=client.recv(1024)


        s=pow(A, b, p)

        SHA=s4_4.SHA1()
        CBCkey=bytes.fromhex(SHA.Hash(bytes([s]))[0:32])
        message=s2_2.CBC_decrypt(client_message, CBCkey, client_IV)
        print("*BOT* | Client Messaage: " + str(message))

        IV=os.urandom(16)
        encrypted_message=s2_2.CBC_encrypt(message, CBCkey, IV)
        client.send(encrypted_message)
        client.send(IV)
        client.close()
        self.bot.close()

def main():
    bot1=Bot(4020)
    bot1.run_bot()

