import socket # importa a biblioteca de sockets
import sys 
import logging # importa a biblioteca para criar logs
from banco import Banco 
from minicoin import MiniCoin
from blockchain import blockchain

# obtém o IP do servidor a partir dos argumentos da linha de comando
if len(sys.argv) > 2:
    ip_servidor = sys.argv[1]
    porta = int(sys.argv[2])
else:
    print("Uso: python3 servidor.py <ip_servidor> <porta>")
    sys.exit(1)
33

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

# vincula o socket à porta 
sock.bind((ip_servidor, porta))
logger.info(f"Socket vinculado à porta {porta}.") 

banco = Banco()  # cria uma instância do Banco
logger.info("Instância do Banco criada com sucesso.")


#Cria a blockchain
bc = blockchain()


# LOOP PRINCIPAL DO SERVIDOR
# vai ficar esperando por conexões
# ao receber uma conexão, ele aceita e cria um novo socket (conn) para se comunicar com o cliente
# ao se conectar, envia uma mensagens do banco e espera por respostas
# trata respostas do cliente, executa ações no banco chamando metodos da blockchain 
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

    if data.decode().upper() == 'S':
        logger.info("Cliente entrou no Banco Central das Minicoins.")
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

            # imprime no servidor o estado atual da blockchain
            print(bc.impressao())
            logger.info(f"Estado atual da blockchain impresso no servidor:\n {bc.impressao()}")


            data = conn.recv(1024)  # recebe a escolha do cliente
            escolha = data.decode()
            logger.info(f"Escolha do cliente {nome}: {escolha}")

            # opcao de ver saldo ---------------------------------------------------
            if escolha == '1':
                saldo = bc.retorna_saldo()
                resposta = banco.saldo_cliente(saldo)
                conn.send(resposta.encode()+banco.menu().encode())
                logger.info(f"Saldo do cliente {nome} foi exibido.")
                print(banco.viu_saldo())


            # opcao de deposito ----------------------------------------------------
            elif escolha == '2':
                mensagem = banco.solicita_deposito()
                conn.send(mensagem.encode())
                data2 = conn.recv(1024)
                movimentacao = data2.decode()
                
                if (bc.numero_movimentacoes() == 0):
                    #Depósito inicial
                    bloco = MiniCoin()
                    bloco.criar_movimentacao(0, nome, int(movimentacao), 0)
                    bc.inserir_bloco(bloco)
                else:
                    novo_bloco = MiniCoin()
                    novo_bloco.criar_movimentacao(int(movimentacao), nome, bc.deposito_inicial(), bc.ultimo_hash())
                    bc.inserir_bloco(novo_bloco)
                
                mensagem = banco.deposito_sucesso()
                conn.send(mensagem.encode()+banco.menu().encode())
                logger.info(f"Confirmação de depósito enviada ao cliente {nome}.")
                print(banco.fez_deposito())


            # opcao de saque -------------------------------------------------------
            elif escolha == '3':
                mensagem = banco.solicita_saque()
                conn.send(mensagem.encode())
                data2 = conn.recv(1024)
                movimentacao = data2.decode()

                if int(movimentacao) > bc.retorna_saldo():
                    mensagem = banco.saldo_insuficiente()
                    conn.send(mensagem.encode()+banco.menu().encode())
                    logger.warning(f"Cliente {nome} não tem saldo suficiente para a operação.")
                    print(banco.saldo_insuficiente())
                else:
                    novo_bloco = MiniCoin()
                    novo_bloco.criar_movimentacao(-int(movimentacao), nome, bc.deposito_inicial(), bc.ultimo_hash())
                    bc.inserir_bloco(novo_bloco)
                    mensagem = banco.saque_sucesso()
                    conn.send(mensagem.encode()+banco.menu().encode())
                    logger.info(f"Confirmação de saque enviada ao cliente {nome}.")
                    print(banco.fez_saque())


            # opcao de sair do banco ------------------------------------------------
            elif escolha == '4':
                resposta = "Saindo do banco. Até logo!"
                conn.send(resposta.encode())
                logger.info("Cliente saiu do banco.")
                conexao = False
                print(banco.encerra_conexao())


            # escolha de opcao invalida do cliente ---------------------------------
            else:
                mensagem = banco.opcao_invalida()
                conn.send(mensagem.encode()+banco.menu().encode())
                logger.info("Enviado aviso de opção inválida ao cliente.")
                print(banco.opcao_invalida())

    else:
        logger.info("Cliente optou por não entrar na conta. Encerrando conexão.")
        print(banco.nao_criou_conta())
        conn.close() # fecha a conexão
        logger.info(f"Conexão com {addr} fechada.")
        print(banco.encerra_conexao())