import os
from menus.voltar_menu import voltar_menu

def mostrar_voos_disponiveis(voos):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Lista de Voos Disponíveis:")
    print("=" * 80)

    for voo in voos:
        print(f"{voo}")
        print(f"Origem: {voo.origem}")
        print(f"Destino: {voo.destino}")
        print(f"Data e Hora: {voo.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print(f"Aeronave: {voo.aviao.modelo} com {voo.aviao.quantidade_assentos} assentos")
        
        assentos_livres = voo.assentos_disponiveis()
        print(f"Assentos disponíveis ({len(assentos_livres)}): {assentos_livres}")

        print("-" * 80)

    voltar_menu()

def mostrar_voos_especificos(voos):
    import random
    os.system('cls')
    print("Mostrando 10 passageiros aleatórios de cada um dos voos:")

    for voo in voos:
        print("="*80)
        print(str(voo))
        print("-"*80)
        if len(voo.passagens) == 0:
            print("Nenhum passageiro alocado neste voo.")
        else:
            amostra = random.sample(voo.passagens, min(10, len(voo.passagens)))
            for passagem in amostra:
                print(f"Assento {passagem.numero_assento} - {passagem.passageiro.nome} ({passagem.passageiro.numero_passaporte})")
        print("="*80 + "\n")

    voltar_menu()