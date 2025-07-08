from entidades.passagem import Passagem
from entidades.pessoa import Passageiro, Tripulante
from datetime import datetime

class Aviao:
    def __init__(self, modelo: str, identificacao: str, companhia: str, quantidade_assentos: int, distancia_maxima_km: int):
        self._modelo = modelo
        self._identificacao = identificacao
        self._companhia = companhia
        self._quantidade_assentos = quantidade_assentos
        self._distancia_maxima_km = distancia_maxima_km

    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def identificacao(self) -> str:
        return self._identificacao

    @property
    def companhia(self) -> str:
        return self._companhia

    @property
    def quantidade_assentos(self) -> int:
        return self._quantidade_assentos

    @property
    def distancia_maxima_km(self) -> int:
        return self._distancia_maxima_km

    def __str__(self) -> str:
        return f"Avião {self._identificacao} - {self._modelo} ({self._companhia})"
    
class Voo:
    def __init__(self, id_voo: str, aviao: Aviao, origem: str, destino: str, data_hora: datetime, tripulacao: list[Tripulante]):
        self.id_voo = id_voo
        self.aviao = aviao
        self.origem = origem
        self.destino = destino
        self.data_hora = data_hora
        self.tripulacao = tripulacao 
        self.passagens: list[Passagem] = []

    def alocar_passageiros(self, lista_passageiros: list[Passageiro]):

        if len(lista_passageiros) > self.aviao.quantidade_assentos:
            print(f"Erro: o voo {self.id_voo} só comporta {self.aviao.quantidade_assentos} passageiros.")
            return

        for idx, passageiro in enumerate(lista_passageiros):
            numero_assento = idx + 1  # assim os assentos vão de 1 a 250
            passagem = Passagem(self, passageiro, numero_assento)
            self.passagens.append(passagem)

    def assentos_disponiveis(self):

        ocupados = [p.numero_assento for p in self.passagens]
        return [i for i in range(1, self.aviao.quantidade_assentos + 1) if i not in ocupados]

    def listar_passageiros(self):

        for p in self.passagens:
            print(f"Assento {p.numero_assento}: {p.passageiro.nome} (Passaporte: {p.passageiro.numero_passaporte})")

    def __str__(self):
        return f"Voo {self.id_voo} | {self.origem} -> {self.destino} | {self.data_hora.strftime('%d/%m/%Y %H:%M')}"