#Faça um Programa que peça dois números e imprima o maior deles.

while True:

    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    if num1 > num2:
      print(f"O maior número é {num1}")
      break

    elif num1 < num2:
      print(f"O maior número é {num2}")
      break

    else:
      print("Os dois números são iguais, tente novamente.")