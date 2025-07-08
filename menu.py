import os

#____________________________________________________________________________________________________

def voltar_menu():
    escolha = input("Digite -> 0 <- para voltar ao menu: ")
    if escolha == "0":
        return  # Volta direto sem mensagem
    while True:
        print("Opção inválida! Digite apenas 0 para voltar.")
        escolha = input("Tente novamente: ")
        if escolha == "0":
            return
        
#____________________________________________________________________________________________________

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
        except ValueError:
            print("Escolha inválida, por favor tente novamente.")
            continue

#____________________________________________________________________________________________________
        if escolha == 1:
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
                        # -criar_passageiro(), provavelmente vai precisar duns input ai-
                        print("Função em desenvolvimento.")
                        voltar_menu()
                    
                    if escolha == 2:
                        #excluir_passageiro()
                        print("Função em desenvolvimento.")
                        voltar_menu()
                except ValueError:
                    print("""
___________________                          
Caractere inválido.
___________________""")
                    
#____________________________________________________________________________________________________

        if escolha == 2:
            # mostrar voos()
            print("Função em desenvolvimento.")
            voltar_menu()

#____________________________________________________________________________________________________

        if escolha == 3:
        # mostrar_passageiros_especificos()
            print("Função em desenvolvimento.")
            voltar_menu()
#____________________________________________________________________________________________________

menu()    