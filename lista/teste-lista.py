'''
TESTANDO A LISTA DA BLOCKCHAIN
'''

from lista import MiniCoin
from lista import blockchain

#Cria a blockchain
bc = blockchain()

print('Número de movimentações: ', bc.numero_movimentacoes())

#Cria um bloco
bloco = MiniCoin()
bloco2 = MiniCoin()
bloco3 = MiniCoin()

#Cria a movimentação
bloco.criar_movimentacao(200, 'Giovanna', bc.numero_movimentacoes(), 0)

#Insere na blockchian
bc.inserir_bloco(bloco)

bloco2.criar_movimentacao(-30, 'Giovanna', bc.numero_movimentacoes(), 0)
bc.inserir_bloco(bloco2)

bloco3.criar_movimentacao(90, 'Giovanna', bc.numero_movimentacoes(), 0)
bc.inserir_bloco(bloco3)

print('\n')

bc.imprime()