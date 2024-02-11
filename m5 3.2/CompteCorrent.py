class CompteCorrent:
    def __init__(self, saldoInicial, cs):
        self.saldo = saldoInicial
        self.contrasenya = cs

    def dipositar(self, pasta: float) -> float:
        self.saldo += pasta
        return self.saldo

    def retirar(self, pasta: float, cs: str) -> float:
        if cs == self.contrasenya and self.saldo >= pasta:
            self.saldo -= pasta
            return self.saldo
        elif cs != self.contrasenya:
            return -2
        else:
            return -1

    def getSaldo(self, cs: str) -> float:
        if cs == self.contrasenya:
            return self.saldo
        else:
            return -2

    def setContrasenya(self, antiga: str, nova: str) -> int:
        if antiga == self.contrasenya:
            self.contrasenya = nova
            return 0
        else:
            return -2
