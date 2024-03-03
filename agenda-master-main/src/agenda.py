from src.contato import Contato
from src.identificador import Identificador


class Agenda:
    def __init__(self):
        self.contatos = []

    def getContatos(self) -> list:
        return self.contatos

    def getQuantidadeDeContatos(self) ->  int:
        return len(self.contatos)

    def getContato(self, nome:str) -> Contato:
        for n in self.contatos:
            if n.getName() == nome:
                return n

    def adicionarContato(self, contato: Contato) -> bool:
        for contact in self.contatos:
            if contact.getName() == contato.getName():
                contact.adicionarFone(contato.getFones())
                return False
        self.contatos.append(contato)
        return True

    def removerContato(self, nome: str) -> bool:
        for n in self.contatos:
            if n.getName() == nome:
                self.contatos.remove(n)
                return True
        return False

    def removerFone(self, nome:str, index: int) -> bool:
        for n in self.contatos:
            if n.getName() == nome:
                self.contatos.remove(n)
                return True
        return False
    def getQuantidadeDeFones(self, identificador: Identificador) -> int:
        return 0

    def getQuantidadeDeFones(self) -> int:
        return 0

    def pesquisar(self, expressao:str) -> list:
        temp_list = []
        for n in self.contatos:
            if expressao in n.getName():
                temp_list.append(n)
            else:
                for f in n.getFones():
                    if expressao in f.getNumero():
                        temp_list.append(n)
        return temp_list