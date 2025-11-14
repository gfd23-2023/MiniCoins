from dataclasses import dataclass           #dataclass é menos verboso do que class e não precisa configurar o __init__
from datetime import datetime               #para o momento de criação da minicoin
from typing import Optional                 #pois o próximo elemento pode existir ou pode ser nulo
import hashlib

#@dataclass transforma uma classe simples em uma estrutura de dados completa com:
#um método __init__ -> criar instâncias
#um método __repr__ -> imprimir de forma legível
#um método __eq__ -> para comparar
#entre outros que podemos definir
#Obs: Os atributos com valor definido devem ficar abaixo dos 'indefinidos'
@dataclass
class MiniCoin:
    movimentacao: int = 0               #Valor da movimentação
    movimentacao_tipo: str = None       #Tipo da movimentação Depósito / Saque
    proprietario: str = None            #Dono da movimentação
    hash_atual: str = None              #Hash em string - menor e mais legível
    criado_em: str = None               #Criação da minicoin - data e horário
    prox: Optional["MiniCoin"] = None   #Próxima movimentação - as aspas permitem autorreferência
    deposito_inicial: int = 0           #Primeiro depósito
    saldo: int = 0
    
    #Métodos

    #self -> representa a instância do objeto
    def gerar_hash(self, hash_bloco_anterior: str):

        #Faz uma string com todas as informações do bloco + o hash antigo
        bloco = f"{self.deposito_inicial}{self.proprietario}{self.movimentacao}{self.criado_em}{hash_bloco_anterior}"

        #Função hash SHA 256 - Simplicidade, legibilidade e segurança
        return hashlib.sha256(bloco.encode()).hexdigest()                #obs: hexdigest gera uma string decimal de 64 caracteres

    #Facilita na passagem do hash como parâmetro para a próxima movimentação
    #O hash atual vira o anterior do próximo bloco
    def retornar_hash(self):
        return self.hash_atual

    def criar_movimentacao(self, valor: int, dono: str, depositoInicial: int, hash_anterior: str):
        #print('Entrei na criação da movimentação')

        self.deposito_inicial = int(depositoInicial)
        self.proprietario = dono
        self.movimentacao = int(valor)                     #mesmo valor, pois o depósito inicial também é uma movimentação
        self.criado_em = datetime.today().isoformat()      #retorna ano-mês-dia hora-minuto-segundo-milissegundo em formato legível
        self.hash_atual = self.gerar_hash(hash_anterior)   #chama o método para a instância atual
        self.prox = None                                   #seta a referência do próximo bloco para nulo
        
        #Tipo da movimentação
        if (valor > 0):
            self.movimentacao_tipo = 'Depósito'
        elif (valor < 0):
            self.movimentacao_tipo = 'Saque'
        elif (valor == 0):
            self.movimentacao_tipo = 'Primeiro Depósito'
        else:
            self.movimentacao_tipo = 'Inválido'
