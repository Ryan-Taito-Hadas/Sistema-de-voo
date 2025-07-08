from entidades.pessoa import Passageiro
from datetime import datetime

class Passagem:
    def __init__(self, voo, passageiro: Passageiro, numero_assento: int):
        """
        Representa a reserva de um assento em um voo.

        :param voo: Objeto da classe Voo.
        :param passageiro: Objeto da classe Passageiro.
        :param numero_assento: Número do assento reservado.
        """
        self._voo = voo
        self._passageiro = passageiro
        self._numero_assento = numero_assento
        self._data_reserva = datetime.now()  # Data da reserva

    @property
    def voo(self):
        return self._voo

    @property
    def passageiro(self):
        return self._passageiro

    @property
    def numero_assento(self):
        return self._numero_assento

    @property
    def data_reserva(self):
        return self._data_reserva

    def __str__(self):
        return (
            f"Passagem para {self.passageiro.nome} | "
            f"Voo: {self.voo.id_voo} | Assento: {self.numero_assento} | "
            f"Data da reserva: {self.data_reserva.strftime('%d/%m/%Y %H:%M')}"
        )