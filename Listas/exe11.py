#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i, j in zip(vetor1, vetor2):
    vetor3 = []
    vetor3.append(i)
    vetor3.append(j)
    print(vetor3)

for i, j, k in zip(vetor1, vetor2, vetor3):
    resultado = []
    resultado.append(i)
    resultado.append(j)
    resultado.append(k)
    print(resultado)