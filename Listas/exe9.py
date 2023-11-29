#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

import numpy as np

vetor = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero**2)

soma = np.sum(vetor)

print(f"{' + '.join(map(str, vetor))} = {soma}.")