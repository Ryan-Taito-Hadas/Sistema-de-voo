from datetime import datetime
from menus.voltar_menu import voltar_menu
from entidades.pessoa import Passageiro
from faker import Faker
from menus.voltar_menu import voltar_menu

faker = Faker('pt_BR')

#___________________________________________________________________________________________

def cadastrar_passageiro(passageiros: list[Passageiro]):
    nome = input("Digite o nome do passageiro: ")
    cpf = input("Digite o CPF: ")

    while True:
        data_nasc_str = input("Digite a data de nascimento (dd/mm/aaaa): ")
        try:
            datetime.strptime(data_nasc_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Data de nascimento inválida. Use o formato dd/mm/aaaa.")
    passaporte = input("Digite o número do passaporte: ")

    p = Passageiro(nome, cpf, data_nasc_str, passaporte)
    passageiros.append(p)
    print("Passageiro cadastrado com sucesso.")
    print(p)
    voltar_menu()

#___________________________________________________________________________________________

def excluir_passageiro(passageiros: list[Passageiro]):
    """
    Exclui um passageiro da lista, buscando pelo CPF.
    """
    if not passageiros:
        print("Nenhum passageiro cadastrado.")
        return

    cpf = input("Digite o CPF do passageiro que deseja excluir: ")

    for passageiro in passageiros:
        if passageiro.cpf == cpf:
            passageiros.remove(passageiro)
            print(f"Passageiro {passageiro.nome} removido com sucesso!")
            return

    print("Nenhum passageiro encontrado com esse CPF.")

#___________________________________________________________________________________________

def menu_passageiro(passageiros: list[Passageiro]):
    while True:
        try:
            escolha = int(input(""" 
_______________________________
|      Menu Passageiro        | 
_______________________________
                  
Selecione a opção desejada:
        
0) Retorne ao Menu
1) Cadastrar novo passageiro
2) Excluir passageiro já criado
________________________________ 

Opção desejada -> """))
            if escolha == 0:
                break
            
            if escolha == 1:
                cadastrar_passageiro(passageiros)

            if escolha == 2:
                excluir_passageiro(passageiros)

        except ValueError:
            print("""
___________________                          
Caractere inválido.
___________________""")
            
#___________________________________________________________________________________________