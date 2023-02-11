from extrato import Extrato

class Conta:
    _total_de_contas = 0
    def __init__(self, clientes, saldo):
        self._total_de_contas += 1
        self.numero = self._total_de_contas
        self.cliente = clientes
        self.saldo = saldo
        self.extrato = Extrato()

    def variavel_de_transacao(self, valor):
        if self.saldo - valor >= 0 or valor > 0:
            return True
        return False

    def saque(self, valor):
        if self.variavel_de_transacao(valor):
            self.saldo -= valor
            self.extrato.registrar_extrato_bancario("saque", self.saldo, -valor)
            return True
        return False

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.registrar_extrato_bancario("deposito", self.saldo, valor)
            return True
        return False

    def tranferencia(self, valor, conta_destino):
        if self.variavel_de_transacao(valor):
            if conta_destino.receber(valor, self.cliente.nome):
                self.saldo -= valor
                self.extrato.registrar_extrato_bancario("tranferencia", self.saldo, -valor, conta_destino.cliente.nome)
                return True
        else:
            False

    def receber(self, valor, remetente):
        if valor > 0:
            self.saldo += valor
            self.extrato.registrar_extrato_bancario("recebimento", self.saldo, valor, remetente, "remetente")
            return True
        return False
