from pprint import pprint


class Cliente:

    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:

    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.total_contas_criadas = (
            30 / ContaCorrente.total_contas_criadas
        )

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


if __name__ == "__main__":
    c1 = Cliente("Doe", "123.456.798-00", "Dev")
    # pprint(c1.__dict__, width=40)
    conta_corrente = ContaCorrente(None, "00", "101")
