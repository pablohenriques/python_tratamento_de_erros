from pprint import pprint
from sqlite3 import OperationalError
from exceptions import OperacaoFinanceiraError, SaldoInsuficienteError


class Cliente:

    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:

    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__set_saldo(100)
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidos = 0
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.total_contas_criadas = (
            30 / ContaCorrente.total_contas_criadas
        )

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser um numero inteiro", value)
        if value <= 0:
            raise ValueError("O atributo agencia deve maior que zero", value)
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo numero deve ser um numero inteiro")
        if value <= 0:
            raise ValueError("O atributo numero deve maior que zero")
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    def __set_saldo(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo saldo deve ser um numero inteiro")
        # if value <= 0:
        #     raise ValueError("O atributo saldo deve maior que zero")
        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError("O valor sacado não pode ser menor que zero")
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            #import traceback
            self.transferencias_nao_permitidos += 1
            #traceback.print_exc()
            E.args = ()
            raise OperacaoFinanceiraError("Operação não finalizada") from E
        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O valor sacado não pode ser menor que zero")
        if self.__saldo < valor:
            self.saques_nao_permitidos += 1
            # raise SaldoInsuficienteError(saldo=self.__saldo, valor=valor)
            # raise SaldoInsuficienteError("Saldo Insuficiente Para Transação")
            raise SaldoInsuficienteError("", self.__saldo, valor)
        self.__saldo -= valor

    def depositar(self, valor):
        self.__set_agencia(valor)

    def __str__(self) -> str:
        return f"Agência: {self.__agencia} - Saldo: {self.__saldo} - Número: {self.__numero}"


def main():
    import sys

    contas = []
    while True:
        try:
            nome = input("Nome do cliente:\n")
            agencia = input("Número de agência:\n")
            # breakpoint()
            numero = input("Numero da conta corrente:\n")
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        except KeyboardInterrupt:
            print(f"\n\n{len(contas)}(s) contas criadas")
            sys.exit()


if __name__ == "__main__":
    conta_corrente1 = ContaCorrente(None, 400, 123465)
    conta_corrente2 = ContaCorrente(None, 200, 654321)

    try:
        #conta_corrente1.transferir(1000, conta_corrente2)
        conta_corrente1.sacar(1000)
        print(f"Conta Corrente 1, saldo: ", conta_corrente1.saldo)
        print(f"Conta Corrente 2, saldo: ", conta_corrente2.saldo)
    except OperacaoFinanceiraError as E:
        # import traceback
        # print(E.saldo)
        # print(E.valor)
        # print("Exceção do tipo:", E.__class__.__name__)
        # traceback.print_exc()
        breakpoint()
        pass
