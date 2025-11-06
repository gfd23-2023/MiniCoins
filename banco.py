# classe que vai conter metodos para simular o banco do servidor
# exibe mensagens para o cliente relacionadas ao banco
class Banco:

    def __init__(self):
        print("⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀")
        print("   💸 BANCO CENTRAL DAS MINICOINS! 💸 ")
        print("⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀\n")


    def bem_vindo(self):
        mensagem = "\n⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀\n💸 BEM VINDO AO BANCO CENTRAL DAS MINICOINS! 💸\n⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀-⛀\n"
        return mensagem
    
    def menu(self):
        mensagem = "\n💰 Escolha uma das opções abaixo:\n\t1 - Ver saldo\n\t2 - Depositar Minicoins\n\t3 - Sacar Minicoins\n\t4 - Sair\n"
        return mensagem

    def cria_conta(self):
        mensagem = "\n🏦 Deseja criar uma conta no Banco Central das Minicoins? (S/N)\n💡 Obs: Você precisa ter uma conta para realizar transações."
        return mensagem

    def conexao(self):
        mensagem = "\n🔌 Um cliente se conectou ao Banco Central das Minicoins!\n"
        return mensagem

    def encerra_conexao(self):
        mensagem = "\n🔌 Conexão do cliente encerrada.\n"
        return mensagem

    def criou_conta(self):
        mensagem = "\n✅ Conta do cliente criada com sucesso!\n"
        return mensagem

    def nao_criou_conta(self):
        mensagem = "\n❌ O cliente optou por não criar uma conta.\n"
        return mensagem
    
