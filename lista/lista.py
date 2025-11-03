""" 
Implementação da lista ligada
OBS: De acordo com o que eu pesquisei, o arquivo __init__.py serve para que o diretório seja
reconhecido como pacote pacote importável. Dentro dele é possível controlar o que é exportado,
agrupar, executar código de configuração, etc.

OBS2: Precisamos passar o self explicitamente na declaração dos métodos das classes, pois nos referimos
à instância que chamou o método. Em outras linguagens isso é implícito, não é o caso do pyhton. Isso acontece 
porque o método precisa acessar o próprio objeto para ler ou alterar os atributos.

OBS3: Pelo que eu li, não faz sentido remover um bloco da blockchain, pois ela é como um registro de movimentações
"""

from dataclasses import dataclass           #dataclass é menos verboso do que class e não precisa configurar o __init__
from datetime import datetime               #para o momento de criação da minicoin
from typing import Optional                 #pois o próximo elemento pode existir ou pode ser nulo
import hashlib                              #utilizar hash como string


#OBS: criar a classe da blockchain com seus respectivos métodos

#@dataclass transforma uma classe simples em uma estrutura de dados completa com:
#um método __init__ -> criar instâncias
#um método __repr__ -> imprimir de forma legível
#um método __eq__ -> para comparar
#entre outros que podemos definir
#Obs: Os atributos com valor definido devem ficar abaixo dos 'indefinidos'
@dataclass
class MiniCoin:
    movimentacao: int = 0               #Valor da movimentação
    proprietario: str = None            #Dono da movimentação
    hash_anterior: str = None           #Hash em string - menor e mais legível
    hash_atual: str = None              #Hash em string - menor e mais legível
    criado_em: str = None               #Criação da minicoin - data e horário
    prox: Optional["MiniCoin"] = None   #Próxima movimentação - as aspas permitem autorreferência
    deposito_inicial: int = 0           #Primeiro depósito
    
    #Métodos

    #self -> representa a instância do objeto
    def gerar_hash(self):

        #Faz uma string com todas as informações do bloco + o hash antigo
        bloco = f"{self.deposito_inicial}{self.proprietario}{self.movimentacao}{self.criado_em}{self.hash_anterior}"

        #Função hash SHA 256 - Simplicidade, legibilidade e segurança
        return hashlib.sha256(bloco.encode()).hexdigest()                #obs: hexdigest gera uma string decimal de 64 caracteres

    #Facilita na passagem do hash como parâmetro para a próxima movimentação
    #O hash atual vira o anterior do próximo bloco
    def retornar_hash_atual(self):
        return self.hash_atual

    def criar_movimentacao(self, valor: int, dono: str, qtd_movimentacoes: int, hash_anterior: str):
        
        #Caso seja a primeira movimentação:
        if (self.deposito_inicial == 0):
            self.deposito_inicial = valor

        self.proprietario = dono
        self.movimentacao = valor                          #mesmo valor, pois o depósito inicial também é uma movimentação
        self.criado_em = datetime.today().isoformat        #retorna ano-mês-dia hora-minuto-segundo-milissegundo em formatp legível

        #A quantidade de movimentações determina se precisamos 'fazer' o primeiro hash ou se podemos
        #apenas pegar o anterior e continuar
        
        #Se a quantidade de movimentações for igual a zero não há bloco anterior, então precisamos criar o primeiro hash
        if (qtd_movimentacoes == 0):
            self.hash_anterior = "0" * 64            #64 zeros -> padrão para o primeiro bloco
        else:
            self.hash_anterior = hash_anterior

        self.hash_atual = self.gerar_hash()     #chama o método para a instância atual



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
            ultimo_bloco = self.head.prox

        ultimo_bloco.prox = bloco

        bloco.prox = None
        self.numero_blocos += 1

        return

#Função para imprimir a blockchain
def imprime_blockchain(bc: blockchain):

    #Cabeça da lista
    print('#')

    #Moedas
    bloco = bc.head

    while (bloco.prox):
        print('-')