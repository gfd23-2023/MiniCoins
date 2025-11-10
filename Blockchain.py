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

    def valida(self):

        print('Entrei na função de validar')        
        #Valida a blockchain inteira
        bloco = self.head

        if self.numero_blocos == 0:
            print('Não há o que validar - Blockchain vazia')
            return

        #Recalcula o hash do primeiro bloco - O HASH ANTERIORO DO PRIMEIRO BLOCO VAI SER ZERO
        hash_original = bloco.retornar_hash()
        bloco.gerar_hash(0)

        if hash_original != bloco.retornar_hash():
            print('⛓️‍💥 Houve violação na Blockchain no bloco 1!!!')
            return None

        hash_anterior = hash_original       #armazena o hash
        
        #Se houver próximo bloco
        if bloco.prox != None:
            bloco = bloco.prox
        else:
            print('️⛓️⛓️✅ Blockchain válida')
            return bloco

        i = 2                           #Segundo bloco em diante
        while bloco.prox is not None:
            #print(bloco)
            hash_original = bloco.retornar_hash()   #pega o hash do bloco atual
            bloco.gerar_hash(hash_anterior)         #recalcula o hash do bloco atual com o hash do bloco anterior
            
            if hash_original != bloco.hash_atual:
                print(f'⛓️‍💥 Houve violação na Blockchain no bloco {i} !!!')
                return 0

            hash_anterior = hash_original
            bloco = bloco.prox
            i += 1

        print('⛓️⛓️✅ Blockchain válida')
        
        #Retorna uma referência para o último bloco
        return bloco

    #Insere um bloco na blockchain - sempre no final
    #Mudar
    def inserir_bloco(self, bloco: MiniCoin):

        #Insere na primeira posição
        if self.head == None:

            self.head = bloco
            self.numero_blocos += 1

            #por garantia
            bloco.prox = None

            return

        #Valida a blockchain para verificar a posibilidade de inserção
        ultimo_bloco = self.valida()

        #print(ultimo_bloco)
        print('Inserindo o novo bloco')
        if ultimo_bloco is not None:
            ultimo_bloco.prox = bloco
            bloco.prox = None
            self.numero_blocos += 1

        return 1

    #Acho que não vai precisar
    def ultimo_hash(self):
        #Percorre a blockchain até chegar no último bloco inserido e retorna o hash
        bloco = self.head

        if self.numero_blocos == 0:
            print("Nenhuma Movimentação")
            return

        while bloco.prox is not None:
            bloco = bloco.prox

        #Retorna uma referência para o último bloco.
        return bloco.hash_atual

    def deposito_inicial(self):
        #Percorre a blockchain até o último bloco inserido e retorna o depósito inicial
        bloco = self.head

        if self.numero_blocos == 0:
            print("Nenhuma Movimentação")
            return

        while bloco.prox is not None:
            print(bloco.deposito_inicial)
            bloco = bloco.prox

        #Retorna uma referência para o último bloco.
        return bloco.deposito_inicial

    #Função para imprimir a blockchain
    def imprime(self):

        #Moedas
        bloco = self.head

        print('----------- Blockchain Inteira: ')

        if (self.numero_blocos == 0):
            print ('Nenhuma Movimentação')
            return

        i = 1
        while bloco is not None:
            print(f'======== BLOCO {i} ========')
            print('Proprietário: ', {bloco.proprietario})
            print('Movimentação: ', {bloco.movimentacao})
            print('Depósito Inicial: ', {bloco.deposito_inicial})
            print('Tipo da Movimentação: ', {bloco.movimentacao_tipo})
            print('==========================')
            i += 1

            bloco = bloco.prox
