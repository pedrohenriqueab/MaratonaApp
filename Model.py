class Pessoa():
    def __init__(self, nome):
        self.nome =  nome

    def falar(self):
        print("falando de forma genérica")

    def andar(self):
        print("andando de forma genérica")

    def pagar(self):
        print("pagando de forma genérica")

class Cliente():
    def __init__(self, nome):
        super(Cliente, self).__init__(nome)

    def pagar(self):
        print("pagando especifiscamente")

class Funcionario():
    def __init__(self, nome):
        super(Funcionario, self).__init__(nome)

class Maratona():
    def __init__(self):
        pass

    def correr():
        Pessoa.andar(Pessoa)
        Pessoa.pagar(Pessoa)

