import socket
from threading import Thread
from config import IP_SERVIDOR, PUERTO

class Cliente:
  def conectar_servidor(self, direccionIP, puerto):
    print(f"Intentando conectar al servidor {direccionIP} y puerto {puerto}")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_cliente:
      socket_cliente.connect((direccionIP,puerto))
      hilo_recibir = Thread(target=self.__recibir, args=(socket_cliente,))
      hilo_enviar = Thread(target=self.__enviar, args=(socket_cliente,))
      
      hilo_recibir.start()
      hilo_enviar.start()
      hilo_recibir.join()
      hilo_enviar.join()
  
  def __enviar(self, socket_cliente):
    while True:
      mensaje = input("\033[0;32;40m>>>")
      socket_cliente.send(mensaje.encode("utf-8", mensaje))
  
  def __recibir(self, socket_cliente):
    while True:
      mensaje = socket_cliente.recv(1024)
      print(f"\033[0;32;40m<<<Mensaje recibido: {mensaje.decode("utf-8")}")

def main():
  cliente: Cliente = Cliente()
  cliente.conectar_servidor(IP_SERVIDOR, PUERTO)

if __name__ == "__main__":
  main()