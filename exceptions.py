class SaldoInsuficienteError(Exception):
    
    def __init__(self, message="", saldo=None, valor=None):
        # breakpoint()
        self.saldo = saldo
        self.valor = valor
        msg = f"Saldo insuficiente para transação\n" \
            f"Saldo Atual: {self.saldo} - Valor de Saque: {self.valor}\n"
        #super(SaldoInsuficienteError, self).__init__(message or msg, self.saldo, self.valor, *args)
        super(SaldoInsuficienteError, self).__init__(message or msg)
