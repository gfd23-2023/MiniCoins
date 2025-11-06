import socket # importa a biblioteca de sockets
import sys 
import logging # importa a biblioteca para criar logs


# configurações do log
# - ele será salvo no arquivo servidor.log
# - o formato do log incluirá data, tipo do log e a mensagem
# - level=logging.INFO garante que chamadas logger.info(...) sejam gravadas
logging.basicConfig(filename='servidor.log', format='%(asctime)s - %(levelname)s - %(message)s', filemode='w', level=logging.INFO) # configura o nível de log (garantindo que logs de nível INFO sejam salvos)
# criamos um objeto (vamos usar ele para criar logs)
logger = logging.getLogger()
logger.info("Iniciando o servidor...") # cria uma mensagem de log


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria o socket TCP
logger.info("Socket criado com sucesso.")
port = 2623 # define a porta

# vincula o socket à porta 
# usamos o endereço de loopback (maquina local)
sock.bind(('localhost', port))
logger.info(f"Socket vinculado à porta {port}.") 

sock.listen() # coloca o socket em modo de escuta
logger.info("Socket agora está em modo de escuta.")

while True:
    # o sock.accept() espera por uma conexão
    # quando uma conexão é feita, ele retorna um novo socket (conn) e o endereço do cliente (addr)
    conn, addr = sock.accept()
    logger.info(f"Conexão aceita de {addr}.") 

    data = conn.recv(1024) # recebe os dados (até 1024 bytes)
    if not data:
        break
    logger.info(f"Dados recebidos: {data.decode()}") # a função decode() converte bytes para string


    conn.close() # fecha a conexão
    logger.info(f"Conexão com {addr} fechada.")