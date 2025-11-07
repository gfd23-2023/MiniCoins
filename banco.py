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
        mensagem = "\n💰 Escolha uma das opções abaixo:\n\t1 - Ver saldo\n\t2 - Depositar Minicoins\n\t3 - Sacar Minicoins\n\t4 - Sair\n\n"
        return mensagem

    def cria_conta(self):
        mensagem = "\n🏦 Deseja criar uma conta no Banco Central das Minicoins? (S/N)\n💡 Obs: Você precisa ter uma conta para realizar transações."
        return mensagem

    def conexao(self):
        mensagem = "🔌 Um cliente se conectou ao Banco Central das Minicoins!\n"
        return mensagem

    def encerra_conexao(self):
        mensagem = "🔌 Conexão do cliente encerrada.\n"
        return mensagem

    def criou_conta(self):
        mensagem = "✅ Conta do cliente criada com sucesso!\n"
        return mensagem

    def nao_criou_conta(self):
        mensagem = "❌ O cliente optou por não criar uma conta.\n"
        return mensagem

    def viu_saldo(self):
        mensagem = "💰 Cliente viu seu saldo com sucesso!\n"
        return mensagem
    
    def fez_deposito(self):
        mensagem = "💸 Cliente fez um depósito com sucesso!\n"
        return mensagem
    
    def fez_saque(self):
        mensagem = "🏧 Cliente fez um saque com sucesso!\n"
        return mensagem
    
    def opcao_invalida(self):
        mensagem = "⚠️ Cliente escolheu uma opção inválida no menu.\n"
        return mensagem

