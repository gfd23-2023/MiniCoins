import socket # importa a biblioteca de sockets
import sys 
import logging # importa a biblioteca para criar logs


# obtém o IP do servidor a partir dos argumentos da linha de comando
if len(sys.argv) > 2:
    ip_servidor = sys.argv[1]
    porta = int(sys.argv[2])
else:
    print("Uso: python3 servidor.py <ip_servidor> <porta>")
    sys.exit(1)


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

sock.connect((ip_servidor, porta))      
logger.info(f"Conectado ao servidor na porta {porta}.")

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