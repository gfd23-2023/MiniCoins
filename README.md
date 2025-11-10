# MiniCoins 💰

**Alunas:**  

|Nome:| GRR |  
|-------------------------------|------  
| Giovanna Fioravante Dalledone |  20232370
| Nadia Luana Lobkov            |  20232381  

**Linguagem Escolhida: Pyhton** 🐍  

## Sumário
1. Início da implementação
2. Cliente-Servidor
3. Chamadas Entre Cliente-Servidor e Blockchain

## 1. Início da Implementação  
Após a escolha da linguagem, foi dado início ao desenvolvimento do trabalho que se deu pela implementação da lista ligada - base da blockchain - e da estrutura cliente-servidor. Enquanto isso, foi possível pesquisar e entender mais sobre a definição de `blockchains` e como utilizar o `hash`.

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