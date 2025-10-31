""" 
Implementação da lista ligada
OBS: De acordo com o que eu pesquisei, o arquivo __init__.py serve para que o diretório seja
reconhecido como pacote pacote importável. Dentro dele é possível controlar o que é exportado,
agrupar, executar código de configuração, etc.
"""

from dataclasses import dataclass           #dataclass é menos verboso do que class e não precisa configurar o __init__
from datetime import datetime               #para o momento de criação da minicoin
import hashlib                              #utilizar hash como string


#OBS: criar a classe da blockchain com seus respectivos métodos

#@dataclass transforma uma classe simples em uma estrutura de dados completa com:
#um método __init__ -> criar instâncias
#um método __repr__ -> imprimir de forma legível
#um método __eq__ -> para comparar
#entre outros que podemos definir
@dataclass
class miniCoin:
    deposito_inicial: int = 0           #Primeiro depósito
    movimentacao: int                   #Valor da movimentação
    proprietario: str                   #Dono da movimentação
    criado_em: datetime                 #Criação da minicoin - data e horário
    hash_anterior: str                  #Hash em string - menor e mais legível
    hash_atual: str                     #Hash em string - menor e mais legível
    ID: int                             #Identificador único da movimentação 
    prox: Optional[miniCoin] = None     #Próxima movimentação

    #Métodos

    #self -> representa a instância do objeto
    def cria_movimentacao(self, valor: int, dono: str):
        
        #Caso seja a primeira movimentação:
        if (self.deposito_inicial == 0):
            self.deposito_inicial = valor

        self.proprietario = dono
        self.movimentacao = valor                #mesmo valor, pois o depósito inicial também é uma movimentação
        #continuar com o tempo e o hash

