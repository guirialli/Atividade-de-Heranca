from cliente import Cliente
from conta import Conta

if __name__ == "__main__":
    c1 = Conta(Cliente("Mario Andrade"), 1000.00)
    c2 = Conta(Cliente("Jessica Andrade"), 500.00)
    c1.deposito(1000)
    c1.saque(100)
    c1.tranferencia(500, c2)