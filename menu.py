import os

def menu():
    while True:

        print ("""
________________________________________________________________________________
|        Boas vindas ao Menu da atividade do Beto sobre reserva de voo         |
________________________________________________________________________________

Selecione a opção desejada:
                         
1) Menu Passageiro
2) Ver lista de Voos disponíveis
3) Ver específicamente 3 passageiros aleatórios de cada um dos 10 Voos criados
               
________________________________________________________________________________
""")

        try:
            escolha = int(input("Minha opção é a -> "))
            os.system('cls') # -Isso aqui serve pra limpar o terminal quando a opção for selecionada-
            
            if escolha == 1:
                escolha = int(input("""
_______________________________
|      Menu Passageiro        | 
_______________________________
                  
Selecione a opção desejada:
        
0) Retorne ao Menu
1) Cadastrar novo passageiro
2) Excluir passageiro já criado
________________________________                                         """))
                if escolha == 0:
                    return 
                if escolha == 1:
                    # -criar_passageiro(), provavelmente vai precisar duns input ai-
                    print("Função em desenvolvimento.")
                    return 
                if escolha == 2:
                    #excluir_passageiro()
                    print("Função em desenvolvimento.")
                    return 
                
        except ValueError:
            print("Escolha inválida, por favor tente novamente.")

menu()    