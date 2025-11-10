# MiniCoins 💰

**Alunas:**  

|Nome:| GRR |  
|-------------------------------|------  
| Giovanna Fioravante Dalledone |  20232370
| Nadia Luana Lobkov            |  20232381  

**Linguagem Escolhida: Pyhton** 🐍  

## Sumário
0. Preparação do ambiente
1. Início da implementação
2. Cliente-Servidor
3. Chamadas Entre Cliente-Servidor e Blockchain

## 1. Início da Implementação  
Após a escolha da linguagem, foi dado início ao desenvolvimento do trabalho que se deu pela implementação da lista ligada - base da blockchain - e da estrutura cliente-servidor. Enquanto isso, foi possível pesquisar e entender mais sobre a definição de `blockchains` e como utilizar o `hash`.



## 0. Preparando o Ambiente 🤖
Para que o código funcione como esperado, execute o seguinte comando:
```
pip install dataclasses

```

## 1. Início da Implementação 🌐
Após a escolha da linguagem, foi dado início ao desenvolvimento do trabalho que se deu pela implementação da lista ligada - base da blockchain - e da estrutura cliente-servidor. Enquanto isso, foi possível pesquisar e entender mais sobre a definição de `blockchains` e como utilizar o `hash`.

> **Importante**: É preciso garantir que o computador tenha instalado uma versão superior ou igual a 3.7 do python ou, pelo menos, que tenha a biblioteca `dataclasses` instalada. Por garantia, executar `pip install dataclasses`.

O desenvolvimento do trabalho teve por início a implementação da lista ligada que representa a Blockchain. Para isso, foram definidas duas classes: `MiniCoins` e `blockchain`.

```Python
@dataclass
class MiniCoin:
    movimentacao: int = 0               #Valor da movimentação
    movmentacao_tipo: str = None        #Tipo da movimentação: Depósito / Saque
    proprietario: str = None            #Dono da movimentação
    hash_atual: str = None              #Hash em string - menor e mais legível
    criado_em: str = None               #Criação da minicoin - data e horário
    prox: Optional["MiniCoin"] = None   #Próxima movimentação - as aspas permitem autorreferência
    deposito_inicial: int = 0           #Primeiro depósito
    saldo: int = 0                      #Saldo atual do usuário

@dataclass
class blockchain:
    head: Optional["MiniCoin"] = None   #Referência para o primeiro elemento da blockchain
    numero_blocos: int = 0              #Número de movimentações

```

A classe `MiniCoins` tem os métodos que manipulam as movimentações financeiras, enquanto isso, a classe `blockchain` tem os métodos que tratam a lista.

**Métodos:**
- Classe `MiniCoins`: `criar_movimentacao`, `gerar_hash`, `retornar_hash`.
- Classe `blockchain`: `numero_movimentacoes`, `inserir_bloco`, `imprime`, `valida`, `deposito_inicial`, `ultimo_hash`.

Dado o contexto de uma blockchain, não havia sentido em implementar uma função de `remover_bloco`, pois o objetivo da lista é manter um registro de todas as movimentações do usuário.

A primeira organização do código foi guardar as classes mencionadas em um primeiro arquivo chamado `lista.py`, porém, depois de conversas, foi chego à conclusão de que seria melhor isolar as classes em arquivos separados, sem a necessidade de uma pasta.

**Pequenos Problemas de Implementação**
Durante os testes, alguns problemas de implementação surgiram:
1. O Depósito Inicial era alterado a cada movimentação. A solução foi criar um método na classe `Blockchain` chamado `deposito_inicial` que retorna o depósito inicial registrado na primeira operação. 
2. A validação utilizando as funções `hash` não funcionava. O problema era extremamente simples, o código não armazenava o retorno do cálculo do hash.

## 2. Cliente-Servidor

## Cliente e Servidor

Para simular o banco usamos um sistema cliente-servidor usando a biblioteca `socket` em Python. Foi criada uma classe auxiliar `Banco` responsável pelas mensagens trocadas na interação, são diversos métodos que retornam mensagens (strings) que o cliente vai receber do servidor, como o banner do banco, instrução para a criação da conta, menu de opções e mensagens de controle do servidor contendo as ações realizadas pelo cliente.

### Fluxo Servidor

O programa `servidor.py` funciona da seguinte maneira:

1. O servidor cria o socket, inicia o banco e entra em um loop para ficar na escuta/espera de conexões.
2. Uma vez que o cliente se conecta, o servidor envia o menu de opções de ações para o cliente.
3. Ao receber a resposta do cliente, ele excecuta o que foi pedido e exibe novamente o menu até o cliente sair.

*Durante esse processo, são impressas mensagens de controle no servidor que informam as ações do cliente.*
   
### Fluxo Cliente

O programa `cliente.py` funciona da seguinte maneira:

1. O cliente cria o socket e se conecta no servidor.
2. Uma vez conectado, ele espera uma mensagem do servidor.
3. Ele verifica de a mensagem é válida (se não é uma de encerramento) e espera o usuário digitar uma entrada como resposta.
4. Ele envia essa resposta ao servidor e volta a esperar um retorno do servidor.

*Todas as mensagens recebidas são impressas para o usuário poder tomar alguma ação.*