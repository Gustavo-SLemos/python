#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

menor = min(num1, num2)
maior = max(num1, num2)

for i in range(menor + 1, maior):
    print(i)