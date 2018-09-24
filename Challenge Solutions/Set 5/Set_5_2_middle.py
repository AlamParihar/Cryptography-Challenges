import socket
import set_4_4 as s4_4
import set_2_2 as s2_2
import random

def main():
    print("Running Middle")
    host=socket.gethostname()
    client_port=3500
    bot_port=4020

    middle_bot=socket.socket()
    middle_client=socket.socket()

    middle_bot.connect((host, bot_port))

    middle_client.bind((host, client_port))
    middle_client.listen()
    client, addr = middle_client.accept()

    status=middle_bot.recv(1024)
    client.send(status)

    p=client.recv(1024)
    g=client.recv(1024)
    A=client.recv(1024)


    middle_bot.send(p)
    middle_bot.send(g)
    middle_bot.send(p)

    B=middle_bot.recv(1024)

    client.send(p)

    client_encrypted=client.recv(1024)
    client_IV=client.recv(1024)

    middle_bot.send(client_encrypted)
    middle_bot.send(client_IV)

    bot_encrypted=middle_bot.recv(1024)
    bot_IV= middle_bot.recv(1024)

    client.send(bot_encrypted)
    client.send(bot_IV)

    s=0
    SHA=s4_4.SHA1()
    CBCkey=bytes.fromhex(SHA.Hash(bytes([s]))[0:32])
    client_message=s2_2.CBC_decrypt(client_encrypted, CBCkey, client_IV)
    bot_message=s2_2.CBC_decrypt(bot_encrypted, CBCkey, bot_IV)

    print("*MITM* | Client Message: " + str(client_message))
    print("*MITM* | Bot Message:    " + str(bot_message))

    client.close()
    middle_bot.close()



