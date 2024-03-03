from src.identificador import Identificador


class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.identificador = identificador
        self.numero = numero

    @staticmethod
    def validarNumero(numero) -> bool:
        for f in numero:
            #0123456789()-
            if f not in ['0', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '(', ')', '-']:
                return False
        return True

    def getIdentificador(self) -> Identificador:
        return self.identificador

    def getNumero(self) -> str:
        return self.numero
