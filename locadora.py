import os

carros = [
  ('Gol', 50),
  ('Palio', 50),
  ('Uno', 50),
  ('Celta', 50),
  ('Fiesta', 50),
  ('Corsa', 50),
  ('Prisma', 50),
  ('Siena', 50),
  ('Fox', 50),
  ('Clio', 50),
  ('Chevette', 50),
  ('Logan', 50)
]

alugados = []

options = [0, 1, 2, 3]


def mostrar_lista_carros(lista_carros):
  print('Carros disponíveis:')
  for i, (carro, valor) in enumerate(lista_carros):
    print(f'[{i}] {carro} - R${valor}/dia')


def menu(opcao):
  if opcao not in options:
    print('Opção inválida! Tente novamente.')
    return
    
  if opcao == 0:
    mostrar_lista_carros(carros)
  elif opcao == 1:
    mostrar_lista_carros(carros)
    print('===============================')
    cod_car = int(input('Escolha o código do carro: '))
    dias = int(input('Quantos dias deseja alugar? '))
    os.system("cls")
    print(f'Você alugou o carro ')
    print(f'O valor total é de R${carros[cod_car][1] * dias}')
    conf = int(input('0 - SIM | 1 - NÃO: '))
    if conf == 0:
      print(f'Parabéns você alugou o {carros[cod_car][0]} por {dias} dias.')
      alugados.append((carros.pop(cod_car), dias))
      print('Carro alugado com sucesso!')
    else:
      print('Aluguel cancelado.')
  elif opcao == 2:
    if len(alugados) == 0:
      print('Nenhum carro alugado.')
      return
    else:
      print('Segue a lista de carros alugados. Qual defeja devolver?')
      mostrar_lista_carros(alugados)
      print('')
      cod = int(input('Escola o código que deseja devolver: '))
      if cod in range(len(alugados)):
        carros.append(alugados.pop(cod)[0])
        print('Carro devolvido com sucesso!')
      else:
        print('Opção inválida! Tente novamente.')
  elif opcao == 3:
    print('Até mais!')
    exit()
  else:
    pass


while True:
  os.system("cls")
  print('===============================')
  print('Bem-vindo a locadora de carros!')
  print('===============================')
  print('O que deseja fazer?')
  print('0 - Mostrar portfólio | 1 - Alugar carro | 2 - Devolver carro | 3 - Sair')
  op = int(input('Digite a opção desejada: '))

  os.system("cls")

  menu(op)
  print('\n')
  print('===============================')
  op = int(input('Digite 0 para voltar ao menu e 3 para sair: '))
  menu(op)
