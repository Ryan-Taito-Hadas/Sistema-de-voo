# Sistema de Reserva de Voos
__________________________________________________________________________________________________________________________________

Este sistema simula a reserva de voos em Python com foco no uso de **Programação Orientada a Objetos (POO)** e dados gerados automaticamente via biblioteca `Faker`. Foi desenvolvido como atividade acadêmica para demonstrar conceitos como encapsulamento, modularização e uso de listas e classes interligadas.

__________________________________________________________________________________________________________________________________
# O que o sistema já faz:

# Geração automática de dados:
- **10 aviões** já são criados ao iniciar o sistema, cada um com modelo, companhia, identificação, capacidade de assentos e distância máxima.
- **10 voos** também são gerados automaticamente, com origem fixada em Campo Grande e destinos variados.
- Cada voo é vinculado a um dos aviões já criados.
- **2480 passageiros** são gerados com nome, CPF, data de nascimento e passaporte.
- Esses passageiros são divididos e **automaticamente alocados nos voos**, respeitando a capacidade de cada avião.
- Cada voo recebe **4 tripulantes** gerados automaticamente (piloto, copiloto e dois comissários).
- Os **assentos são atribuídos aleatoriamente** de 1 a 250, evitando sobras previsíveis.

# Funcionalidades no menu:
- **Menu Passageiro**:
- Permite criar passageiros manualmente.
- Permite excluir passageiros da lista.
- (*Ainda não é possível associar um passageiro manualmente criado a um voo.*)

- **Menu Ver Voos Disponíveis**:
  - Lista todos os 10 voos criados.
  - Mostra origem, destino, data, avião utilizado e **quantos e quais assentos ainda estão disponíveis**.

- **Menu Ver 10 Passageiros Aleatórios por Voo**:
  - Para cada voo, seleciona e exibe 10 passageiros aleatórios que já foram alocados.

__________________________________________________________________________________________________________________________________

# Como executar:

1. Instale o Python 3.11+.
2. Instale a biblioteca `Faker`:

```bash
pip install faker

(_________________________________________________________________________________________________________________________________)