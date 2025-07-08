#______________________________________________________________________________________

def voltar_menu():
    escolha = input("Digite -> 0 <- para voltar ao menu: ")
    if escolha == "0":
        return  # pra voltar direto sem mensagem
    while True:
        print("Opção inválida! Digite apenas 0 para voltar.")
        escolha = input("Tente novamente: ")
        if escolha == "0":
            return
        
#______________________________________________________________________________________