#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

while True:

    numero = int(input("Digite um número de 1 a 10 para sua tabuada: "))
    if numero >0 and numero <= 10:
      print(f"Tabuada do {numero}:")
      for i in range(1, 11):
        multiplica = numero * i
        print(f"{numero} X {i} = {multiplica}")
      break
    else:
      print("Número inválido, tente novamente com um número entre 1 e 10!")

    