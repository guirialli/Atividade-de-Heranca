import datetime

class Extrato:
    def __init__(self):
        self.extratos = []
    def registrar_extrato_bancario(self, operacao, saldo, movimento, destinatario=None, quem_destina="destinatario"):
        if destinatario:
            extrato = {"data": datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S"),
                       "operacao": operacao,
                       quem_destina: destinatario,
                       "saldo anterior": movimento + saldo,
                       "movimentado": movimento,
                       "saldo final": saldo}
        else:
            extrato = {"data": datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S"),
                       "operacao": operacao,
                       "saldo anterior": movimento + saldo,
                       "movimentado": movimento,
                       "saldo final": saldo}

        self.extratos.append(extrato)
        self.ler_extrato(extrato)
        print(f'\n\n')

    def ler_extratos(self):
        for extrato in self.extratos:
            print(f"\n=================\n")
            self.ler_extrato(extrato)
            print(f"\n=================\n")

    @classmethod
    def ler_extrato(cls, extrato=None):
        if extrato is None:
            extrato = {}
        for k, v in extrato.items():
            print(f'{k}: {v}')

