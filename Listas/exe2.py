#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

for numeros in range(10):
    numeros = float(input("Digite um número real: "))
    lista.append(numeros)

lista.sort(reverse=True)
print(lista)