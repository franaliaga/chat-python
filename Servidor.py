import socket
from threading import Thread
from config import IP_SERVIDOR, PUERTO

class Servidor:
  def __init__(self, direccionIP: str, puerto: int) -> None:
    self.direccionIP = direccionIP
    self.puerto = puerto
  
  def esperar_cliente(self):
    print(f"Escuchando en el puerto {self.puerto} de la direccion {self.direccionIP}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_servidor:
      socket_servidor.bind((self.direccionIP, self.puerto))
      socket_servidor.listen()
      socket_cliente, direccion_remota = socket_servidor.accept()
      print(f"Cliente conectado desde la direccion {direccion_remota}")
      
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
      print("\n" + f"\033[0;34;40m<<<Mensaje recibido: {mensaje.decode("utf-8")}")

def main():
  servidor: Servidor = Servidor(IP_SERVIDOR, PUERTO)
  servidor.esperar_cliente()

if __name__ == "__main__":
  main()