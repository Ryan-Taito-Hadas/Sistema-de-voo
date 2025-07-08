from faker import Faker
from entidades import Passageiro, Tripulante

faker = Faker('pt_BR') #Pra criação de dados BR

for i in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    data_nasc = faker.date_of_birth(minimum_age=18, maximum_age=65).strftime('%d/%m/%Y')
    passaporte = faker.bothify(text='??######')
    p = Passageiro(nome, cpf, data_nasc, passaporte)

    
    print(p)

