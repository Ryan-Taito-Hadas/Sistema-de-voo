import os
from entidades.aviao import Voo
from menus.menu_passageiro import menu_passageiro
from menus.voltar_menu import voltar_menu
from entidades.pessoa import Passageiro
from mostrar_voos import mostrar_voos_disponiveis, mostrar_voos_especificos

#___________________________________________________________________________________________

def menu(passageiros: list[Passageiro], voos: list[Voo]):
    while True:
        print ("""
________________________________________________________________________________
|        Boas vindas ao Menu da atividade do Beto sobre reserva de voo         |
________________________________________________________________________________

Selecione a opção desejada:
                         
1) Menu Passageiro
2) Ver lista de Voos disponíveis
3) Ver específicamente 10 passageiros aleatórios de cada um dos 10 Voos criados
               
________________________________________________________________________________
""")

        try:
            escolha = int(input("Minha opção é a -> "))
            os.system('cls')
        except ValueError:
            print("Escolha inválida, por favor tente novamente.")
            continue

        if escolha == 1:
            menu_passageiro(passageiros, voos)

        elif escolha == 2:
            mostrar_voos_disponiveis(voos)

        elif escolha == 3:
            mostrar_voos_especificos(voos)

#___________________________________________________________________________________________
