#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

while True:

    valor = int(input("Digite um número positivo ou negativo: "))

    if valor > 0:
      print("O valor digitado é positivo.")
      break
    elif valor < 0:
      print("O valor digitado é negativo.")
      break
    else:
       print("O valor zero não é válido, tente novamente.")