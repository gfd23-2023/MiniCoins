from dataclasses import dataclass           #dataclass é menos verboso do que class e não precisa configurar o __init__
from typing import Optional                 #pois o próximo elemento pode existir ou pode ser nulo
from Minicoin import MiniCoin

@dataclass
class blockchain:
    head: Optional["MiniCoin"] = None            #referência para o primeiro elemento da blockchain
    numero_blocos: int = 0                       #número de movimentações

    #Métodos
    def numero_movimentacoes(self):
        return self.numero_blocos

    #Insere um bloco na blockchain - sempre no final
    def inserir_bloco(self, bloco: MiniCoin):

        #Insere na primeira posição
        if self.head == None:

            self.head = bloco
            self.numero_blocos += 1

            #por garantia
            bloco.prox = None

            return

        #Caminha até a última posição
        ultimo_bloco = self.head
        while (ultimo_bloco.prox != None):
            ultimo_bloco = ultimo_bloco.prox

        ultimo_bloco.prox = bloco

        bloco.prox = None
        self.numero_blocos += 1

        return

    def valida(self, minicoin: MiniCoin):
        
        #Valida a blockchain inteira
        bloco = self.head

        #Recalcula o hash do primeiro bloco - O HASH ANTERIORO DO PRIMEIRO BLOCO VAI SER ZERO
        hash_original = bloco.retornar_hash()
        bloco.gerar_hash(0)

        if hash_original != bloco.hash_atual():
            print('⛓️‍💥 Houve violação na Blockchain no bloco 1!!!')
            return 0

        hash_anterior = hash_original       #armazena o hash
        bloco = bloco.prox()
        int i = 2                           #Segundo bloco em diante
        while bloco is not None:
            hash_original = bloco.retornar_hash()   #pega o hash do bloco atual
            bloco.gerar_hash(hash_anterior)         #recalcula o hash do bloco atual com o hash do bloco anterior
            
            if hash_original != bloco.hash_atual:
                print('⛓️‍💥 Houve violação na Blockchain no bloco '+ i '!!!')
                return 0

            hash_anterior = hash_original
            bloco = bloco.prox
            i += 1

        print('⛓️ Blockchain válida')
        return 1


    #Função para imprimir a blockchain
    def imprime(self):

        #Moedas
        bloco = self.head

        print('Blockchain:')
        int i = 1
        while bloco is not None:
            print('===== BLOCO ' + i + ' ====')
            print('Proprietário: ', {bloco.proprietario})
            print('Movimentação: ', {bloco.movimentacao})
            print('Tipo da Movimentação: ', {bloco.movimentacao_tipo})
            print('==========================')
            i += 1

            bloco = bloco.prox
