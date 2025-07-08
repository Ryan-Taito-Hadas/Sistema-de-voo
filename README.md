# Sistema de Reserva de Voos

Este projeto é um sistema de reserva de voos desenvolvido em Python como atividade acadêmica. O foco principal é aplicar conceitos de Programação Orientada a Objetos (POO), como encapsulamento, modularização e interação entre classes. O sistema também utiliza a biblioteca Faker para gerar dados automáticos.

# Funcionalidades do sistema
Geração automática de dados

-10 aviões são criados ao iniciar o sistema, cada um com modelo, companhia, capacidade de assentos e distância máxima.
-10 voos são gerados automaticamente, com origem em Campo Grande e destinos variados.
-Cada voo é vinculado a um dos aviões.
-2480 passageiros são criados com nome, CPF, data de nascimento e passaporte. (2 assentos disponíveis em cada voo pra possibilitar a criação e alocação manual de um passageiro.)
-Os passageiros são automaticamente distribuídos entre os voos, respeitando a capacidade dos aviões.
-Cada voo recebe 4 tripulantes gerados automaticamente (piloto, copiloto e dois comissários).
-Assentos são atribuídos aleatoriamente de 1 a 250 para cada voo.

# Menu Passageiro

-Permite cadastrar novos passageiros manualmente.
-Permite excluir passageiros.
-Permite reservar um assento para um passageiro em um voo disponível.

# Menu de Voos

-Exibe os 10 voos criados com detalhes como origem, destino, data e avião.
-Mostra os assentos disponíveis em cada voo.
-Visualização de Passageiros
-Para cada voo, exibe 10 passageiros aleatórios já alocados.

### Como executar

Instale o Python 3.11 ou superior.

Instale a biblioteca Faker:

Execute o arquivo main.py para iniciar o sistema.