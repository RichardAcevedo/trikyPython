import sys
import socket as sk

host = "127.0.0.1"
port = 8090

sCliente = sk.socket()
sCliente.connect((host, port))
print("Conectado")

entrada = sCliente.recv(512) 
mensajeEnviar = entrada.decode("UTF8")
print("Servidor retorna:", mensajeEnviar)

inp = input("El nombre del usuario es: ")
salida = inp.encode("UTF8")
sCliente.send("Lorem Ipsum dolor".encode("UTF8"))

sCliente.close()
print("Terminado")
