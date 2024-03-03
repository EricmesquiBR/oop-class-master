class Conta:
    def __init__(self, numero:int, saldo:float):
        self.numero = numero
        self.limite = 100
        self.saldo = saldo + self.limite
        self.extrato = []

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return self.limite

    def sacar(self, valor: float):
        if self.saldo - valor < 0 or valor < 0 or len(self.extrato) == 10:
            return False
        else:
            if valor > self.saldo - self.limite:
                self.limite = self.limite - (valor - (self.saldo - self.limite))
            self.saldo -= valor
            self.extrato.append(-valor)
            return True

    def depositar(self, valor: float):
        if valor < 0 or len(self.extrato) == 10:
            return False
        else:
            self.saldo += valor
            if self.limite < 100:
                if valor + self.limite > 100:
                    self.limite = 100

                else:
                    self.limite += valor

            self.extrato.append(valor)
            return True

    def transferir(self, destino, valor:float):
        if self.saldo - valor < 0 or valor < 0 or len(self.extrato) == 10:
            return False
        elif not isinstance(destino, Conta):
            return False
        else:
            if valor > self.saldo - self.limite:
                self.limite = self.limite - (valor - (self.saldo - self.limite))
            self.saldo -= valor
            self.extrato.append(-valor)
            destino.depositar(valor)


            return True

    def verExtrato(self):
        return self.extrato