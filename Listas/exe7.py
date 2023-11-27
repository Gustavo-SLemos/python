#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

import numpy as np

vetor = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

soma_vetor  =  np.sum(vetor)
multiplicacao_vetor = np.prod(vetor)
media = np.median(vetor)

print(f"A soma do vetor é {soma_vetor}.")
print(f"A multiplicação do vetor é {multiplicacao_vetor}.")
print(f"Os números do vetor são {vetor}.")
print(f"A média é {media}.")