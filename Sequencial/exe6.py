#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Digite o raio de um círculo: "))
area = round(math.pi * (raio ** 2), 2)

print(f"A área do círculo é: {area}")