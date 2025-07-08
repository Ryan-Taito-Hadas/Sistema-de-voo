from datetime import datetime
from entidades.pessoa import Passageiro

#______________________________________________________________________________________________________________________________

class Passagem:
    def __init__(self, voo, passageiro: Passageiro, numero_assento: int):
        self._voo = voo
        self._passageiro = passageiro
        self._numero_assento = numero_assento
        self._data_reserva = datetime.now()

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
            f"Data: {self.data_reserva.strftime('%d/%m/%Y %H:%M')}"
        )

#______________________________________________________________________________________________________________________________

def reservar_voo_para_passageiro(passageiros, voos):
    from entidades.passagem import Passagem

    print("""
PASSAGEIROS DISPONÍVEIS PARA RESERVA:
""")
    passageiros_disponiveis = [
        p for p in passageiros
        if not any(p is passagem.passageiro for voo in voos for passagem in voo.passagens)
    ]

    if not passageiros_disponiveis:
        print("""
______________________________________              
Todos os passageiros já estão em voos.
______________________________________""")
        return

    for i, p in enumerate(passageiros_disponiveis):
        print(f"{i + 1}) {p.nome} - Passaporte: {p.numero_passaporte}")

    try:
        escolha_p = int(input("Escolha o passageiro pelo número: ")) - 1
        passageiro = passageiros_disponiveis[escolha_p]
    except (IndexError, ValueError):
        print("""
_____Escolha inválida._____
_____Retornando ao Menu____""")
        return

    print("\nVOOS DISPONÍVEIS:")
    for i, v in enumerate(voos):
        print(f"{i + 1}) Voo {v.id_voo} para {v.destino} em {v.data_hora.strftime('%d/%m/%Y %H:%M')}")

    try:
        escolha_v = int(input("""
Escolha o voo pelo número
_________________________
Minha escolha -> """)) - 1
        voo = voos[escolha_v]
    except (IndexError, ValueError):
        print("""
_____Escolha inválida._____
_____Retornando ao Menu____""")
        return

    assentos_livres = voo.assentos_disponiveis()
    if not assentos_livres:
        print("""
_____Não há assentos.______
_____Retornando ao Menu____""")
        return

    print("""
Assentos disponíveis:
_____________________""")
    print(assentos_livres)

    try:
        numero_assento = int(input("Escolha um número de assento disponível: "))
        if numero_assento not in assentos_livres:
            print("""
___Assento indisponível.___
_____Retornando ao Menu____""")
            return
    except ValueError:
        print("""
_____Escolha inválida._____
_____Retornando ao Menu____""")
        return

    passagem = Passagem(voo, passageiro, numero_assento)
    voo.passagens.append(passagem)

    print("""
_______________________________
Passagem reservada com sucesso!
_______________________________""")
    print(passagem)

#______________________________________________________________________________________________________________________________