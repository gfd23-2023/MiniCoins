import socket # importa a biblioteca de sockets
import sys 
import logging # importa a biblioteca para criar logs
from banco import Banco 
from minicoin import MiniCoin
from blockchain import blockchain


# configurações do log
# - ele será salvo no arquivo servidor.log
# - o formato do log incluirá data, tipo do log e a mensagem
# - level=logging.INFO garante que chamadas logger.info(...) sejam gravadas
logging.basicConfig(filename='servidor.log', format='%(asctime)s - %(levelname)s - %(message)s', filemode='w', level=logging.INFO) # configura o nível de log (garantindo que logs de nível INFO sejam salvos)
# criamos um objeto (vamos usar ele para criar logs)
logger = logging.getLogger()
logger.info("Iniciando o servidor...") # cria uma mensagem de log

# cria o socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logger.info("Socket criado com sucesso.")
port = 2623 # define a porta

# vincula o socket à porta 
# usamos o endereço de loopback (maquina local)
#sock.bind(('10.254.221.73', port)) #ufpr
sock.bind(('192.168.100.5', port))  #casa
logger.info(f"Socket vinculado à porta {port}.") 

banco = Banco()  # cria uma instância do Banco
logger.info("Instância do Banco criada com sucesso.")


#Cria a blockchain
bc = blockchain()

while True:
    sock.listen() # coloca o socket em modo de escuta
    logger.info("Socket agora está em modo de escuta.")

    # o sock.accept() espera por uma conexão
    # quando uma conexão é feita, ele retorna um novo socket (conn) e o endereço do cliente (addr)
    conn, addr = sock.accept()
    logger.info(f"Conexão aceita de {addr}.") 
    print(banco.conexao())

    # envia mensagem de boas-vindas ao cliente
    conn.send(banco.bem_vindo().encode()+banco.cria_conta().encode())
    data = conn.recv(1024) # recebe uma resposta (até 1024 bytes)
    logger.info(f"Dados recebidos do cliente: {data.decode()}")

    nome = ''
    if data.decode().upper() == 'S':
        logger.info("Cliente optou por criar uma conta.")
        print(banco.criou_conta())

        mensagem = "Digite seu nome: "
        conn.send(mensagem.encode())
        data = conn.recv(1024)
        nome = data.decode()
        
        # envia o menu ao cliente
        conn.send(banco.menu().encode())  
        logger.info("Menu enviado ao cliente.")

        conexao = True
        while conexao:
            data = conn.recv(1024)  # recebe a escolha do cliente
            escolha = data.decode()
            logger.info(f"Escolha do cliente: {escolha}")

            if escolha == '1':
                saldo = bc.retorna_saldo()
                resposta = "Seu saldo é de {} Minicoins.".format(saldo)
                conn.send(resposta.encode()+banco.menu().encode())
                logger.info("Enviado saldo ao cliente.")
                print(banco.viu_saldo())
            elif escolha == '2':
                mensagem = "Digite o valor que deseja depositar: "
                conn.send(mensagem.encode())
                data2 = conn.recv(1024)
                movimentacao = data2.decode()
                
                if (bc.numero_movimentacoes() == 0):
                    #Depósito inicial
                    bloco = MiniCoin()
                    bloco.criar_movimentacao(0, nome, bc.numero_movimentacoes(), int(movimentacao), 0)
                    bc.inserir_bloco(bloco)
                else:
                    novo_bloco = MiniCoin()
                    novo_bloco.criar_movimentacao(int(movimentacao), nome, bc.numero_movimentacoes(), bc.deposito_inicial(), bc.ultimo_hash())
                    bc.inserir_bloco(novo_bloco)
                
                resposta = "Depósito realizado com sucesso."
                conn.send(resposta.encode()+banco.menu().encode())
                logger.info("Confirmação de depósito enviada ao cliente.")
                print(banco.fez_deposito())
            elif escolha == '3':
                mensagem = "Digite o valor que deseja retirar: "
                conn.send(mensagem.encode())
                data2 = conn.recv(1024)
                movimentacao = data2.decode()

                if int(movimentacao) > bc.retorna_saldo():
                    resposta = "Saldo insuficiente!"
                    conn.send(resposta.encode())
                else:
                    novo_bloco = MiniCoin()
                    novo_bloco.criar_movimentacao(-int(movimentacao), nome, bc.numero_movimentacoes(), bc.deposito_inicial(), bc.ultimo_hash())
                    bc.inserir_bloco(novo_bloco)
                    resposta = "Saque realizado com sucesso."
                    conn.send(resposta.encode()+banco.menu().encode())
                    logger.info("Confirmação de saque enviada ao cliente.")
                    print(banco.fez_saque())
            elif escolha == '4':
                resposta = "Saindo do banco. Até logo!"
                conn.send(resposta.encode())
                logger.info("Cliente saiu do banco.")
                conexao = False
                print(banco.encerra_conexao())
            else:
                resposta = "Opção inválida. Tente novamente."
                conn.send(resposta.encode()+banco.menu().encode())
                logger.info("Enviado aviso de opção inválida ao cliente.")
                print(banco.opcao_invalida())

    else:
        logger.info("Cliente optou por não criar uma conta. Encerrando conexão.")     
        print(banco.nao_criou_conta())
        conn.close() # fecha a conexão
        logger.info(f"Conexão com {addr} fechada.")
        print(banco.encerra_conexao())