#Faça um programa que leia 5 números e informe o maior número.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

print(max(num1, num2, num3, num4, num5))

#ou

#numeros = []

#for i in range(5):
#    numero = float(input(f"Digite o {i+1} número: "))
#    numeros.append(numero)

#print(max(numeros))