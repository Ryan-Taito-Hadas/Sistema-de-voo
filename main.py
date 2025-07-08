from entidades.pessoa import Passageiro
from gerador import gerar_passageiros_e_voos
from menus.menu_principal import menu

passageiros: list[Passageiro] = []

#______________________________________________________________________________________

if __name__ == "__main__":

    voos = gerar_passageiros_e_voos(passageiros)
    menu(passageiros, voos)

#______________________________________________________________________________________
