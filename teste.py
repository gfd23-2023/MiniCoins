from minicoin import MiniCoin
from blockchain import blockchain

#Cria a blockchain
bc = blockchain()

bc.imprime()

#Cria os blocos
bloco1 = MiniCoin()
bloco2 = MiniCoin()
bloco3 = MiniCoin()
bloco4 = MiniCoin()

#Cria a movimentação
bloco1.criar_movimentacao(0, 'Giovanna', bc.numero_movimentacoes(), 500, 0)

#Insere na blockchain
bc.inserir_bloco(bloco1)

#Imprime
#bc.imprime()

#print(f"Depósito Inicial arquivo teste.py depois de inserir o primeiro bloco: {bc.deposito_inicial()}")

#Segunda movimentação
bloco2.criar_movimentacao(-20, 'Giovanna', bc.numero_movimentacoes(), bc.deposito_inicial(), bc.ultimo_hash())
bc.inserir_bloco(bloco2)
#bc.imprime()

#print(f"Depósito Inicial arquivo teste.py: {bc.deposito_inicial()}")

#Terceira movimentação
bloco3.criar_movimentacao(-45, 'Giovamma', bc.numero_movimentacoes(), bc.deposito_inicial(), bc.ultimo_hash())
bc.inserir_bloco(bloco3)
#bc.imprime()

#Simulando violação
#bloco2.deposito_inicial = 1000

#Quarta movimentação
bloco4.criar_movimentacao(100, 'Giovanna', bc.numero_movimentacoes(), bc.deposito_inicial(), bc.ultimo_hash())
bc.inserir_bloco(bloco4)
bc.imprime()

#print(f"Depósito Inicial: {bc.deposito_inicial()}")