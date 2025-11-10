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

sock.connect(('10.254.237.4', port)) # conecta ao servidor
logger.info(f"Conectado ao servidor na porta {port}.")

conexao = True
while conexao:

    mensagem = sock.recv(1024) # recebe os dados do servidor (até 1024 bytes)
    if not mensagem:
        conexao = False
        break
    if mensagem.decode() == "Saindo do banco. Até logo!":
        conexao = False
        break

    print(mensagem.decode()) # exibe a mensagem recebida do servidor
    logger.info(f"Dados recebidos do servidor: {mensagem.decode()}") # a função decode() converte bytes para string

    user_input = input("➤ ")  # lê a entrada do usuário
    sock.send(user_input.encode())  # envia a entrada do usuário ao servidor
    logger.info(f"Dados enviados ao servidor: {user_input}")


sock.close() # fecha o socket
logger.info("Socket fechado.")