import socket # importa a biblioteca de sockets
import sys 
import logging # importa a biblioteca para criar logs


# configurações do log
# - ele será salvo no arquivo cliente.log
# - o formato do log incluirá data, tipo do log e a mensagem
# - level=logging.INFO garante que chamadas logger.info(...) sejam gravadas
logging.basicConfig(filename='cliente.log', format='%(asctime)s - %(levelname)s - %(message)s', filemode='w', level=logging.INFO) # configura o nível de log
# criamos um objeto (vamos usar ele para criar logs)
logger = logging.getLogger()
logger.info("Iniciando o cliente...") # cria uma mensagem de log

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria o socket TCP
logger.info("Socket criado com sucesso.")
port = 2623 # define a porta

sock.connect(('localhost', port)) # conecta ao servidor
logger.info(f"Conectado ao servidor na porta {port}.")

message = "oii servidor! aqui eh o cliente :)" # mensagem a ser enviada
sock.send(message.encode()) # envia a mensagem (a função encode() converte string para bytes)
logger.info(f"Mensagem enviada: {message}")
sock.close() # fecha o socket
logger.info("Socket fechado.")