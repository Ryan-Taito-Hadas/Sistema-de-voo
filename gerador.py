from faker import Faker
from entidades.pessoa import Passageiro, Tripulante
from entidades.aviao import Aviao
from entidades.aviao import Voo
from datetime import datetime, timedelta

faker = Faker("pt_BR")

#______________________________________________________________________________________

def gerar_passageiros_e_voos(passageiros: list[Passageiro]) -> list[Voo]:

    modelos = [
    ("Boeing 737", 250, 5000),
    ("Airbus A320", 250, 4800),
    ("Embraer E195", 250, 3000),
    ("Boeing 787", 250, 8000),
    ("Airbus A330", 250, 7200),
    ("ATR 72", 250, 1500),
    ("Boeing 777", 250, 9000),
    ("Airbus A350", 250, 8500),
    ("Embraer E190", 250, 2900),
    ("Boeing 767", 250, 6400)
]

    avioes = []

    for i, (modelo, assentos, distancia) in enumerate(modelos):
        identificacao = f"AV{i+1:03}"
        companhia = faker.company()
        aviao = Aviao(modelo, identificacao, companhia, assentos, distancia)
        avioes.append(aviao)

    for _ in range(2480):
        nome = faker.name()
        cpf = faker.cpf()
        data_nasc = faker.date_of_birth(minimum_age=18, maximum_age=65).strftime('%d/%m/%Y')
        passaporte = faker.bothify(text="??######")
        p = Passageiro(nome, cpf, data_nasc, passaporte)
        passageiros.append(p)

    destinos = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador",
                "Recife", "Curitiba", "Porto Alegre", "Fortaleza", "Manaus"]
    
    voos: list[Voo] = []
    for i in range(10):
        aviao = avioes[i]
        data_hora = datetime.now() + timedelta(days=i)
        origem = "Campo Grande"
        destino = destinos[i]

        tripulacao = [
            Tripulante(faker.name(), faker.cpf(), faker.date_of_birth(minimum_age=30, maximum_age=60).strftime('%d/%m/%Y'), "Piloto"),
            Tripulante(faker.name(), faker.cpf(), faker.date_of_birth(minimum_age=30, maximum_age=60).strftime('%d/%m/%Y'), "Copiloto"),
            Tripulante(faker.name(), faker.cpf(), faker.date_of_birth(minimum_age=30, maximum_age=60).strftime('%d/%m/%Y'), "Comissário"),
            Tripulante(faker.name(), faker.cpf(), faker.date_of_birth(minimum_age=30, maximum_age=60).strftime('%d/%m/%Y'), "Comissário")
        ]

        voo = Voo(f"V{i+1}", aviao, origem, destino, data_hora, tripulacao)

        passageiros_voo = passageiros[i*248:(i+1)*248]
        voo.alocar_passageiros(passageiros_voo)

        voos.append(voo)

    return voos

#______________________________________________________________________________________