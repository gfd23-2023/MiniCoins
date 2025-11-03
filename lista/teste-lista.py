'''
TESTANDO A LISTA DA BLOCKCHAIN
'''

from lista import MiniCoin
from lista import blockchain
from lista import imprime_blockchain

#Cria a blockchain
bc = blockchain()

#Cria um bloco
bloco = MiniCoin()

#Cria a movimentação
bloco = bloco.criar_movimentacao(200, 'Giovanna', bc.numero_movimentacoes(), 0)

imprime_blockchain(bc)