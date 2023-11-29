#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i, j in zip(vetor1, vetor2):
    vetor3 = []
    vetor3.append(i)
    vetor3.append(j)
    print(vetor3)