class Pessoa:
    def __init__(self, nome: str, cpf: str, data_nascimento: str):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self._data_nascimento = value

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"

class Tripulante(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, tipo: str):
        super().__init__(nome, cpf, data_nascimento)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    def __str__(self):
        return f"{self.nome} - Tripulante ({self.tipo})"

class Passageiro(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, numero_passaporte: str):
        super().__init__(nome, cpf, data_nascimento)
        self._numero_passaporte = numero_passaporte

    @property
    def numero_passaporte(self):
        return self._numero_passaporte

    @numero_passaporte.setter
    def numero_passaporte(self, value):
        self._numero_passaporte = value

    def __str__(self):
        return f"{self.nome} - Passageiro (Passaporte: {self.numero_passaporte})"

