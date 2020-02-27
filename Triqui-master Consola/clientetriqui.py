import sys
import socket as sk
from jugador import *

host="localhost"
puerto=2000

cliente=sk.socket()
cliente.connect((host, puerto))
print("Conectado...")

while True:
	#Enviar nombre del jugador 
	jugador.nombre=input("Ingrese su nombre: ")
	print("Enviar: ", jugador.nombre)
	salida=jugador.nombre.encode("UTF8")
	print("Objeto a enviar: ", salida.decode("UTF8"))
	enviar=cliente.send(salida)

	#Enviar tablero
	print("Enviar: ", jugador.tablero)
	salida=jugador.tablero.encode("UTF8")
	print("Objeto a enviar: ", salida.decode("UTF8"))
	enviar=cliente.send(salida)

	#Enviar movimientos del jugador
	jugador.fila=input("Ingrese la fila a seleccionar: ")
	print("Enviar: ", jugador.fila)
	salida=jugador.fila.encode("UTF8")
	print("Objeto a enviar: ", salida.decode("UTF8"))
	enviar=cliente.send(salida)
	jugador.col=input("Ingrese la columna a seleccionar: ")
	print("Enviar: ", jugador.col)
	salida=jugador.col.encode("UTF8")
	print("Objeto a enviar: ", salida.decode("UTF8"))
	enviar=cliente.send(salida)

	#Recibir respuesta del servidor
	respuesta=cliente.recv(512)
	respuestaServidor=respuesta.decode("UTF8")
	print("Servidor envia: ",respuestaServidor)

	"""if entrada=="exit":
		break"""

cliente.close()
print("Conexion terminada")		