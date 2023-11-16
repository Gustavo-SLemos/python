#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

for numeros in range(5):
    numeros = int(input("Digite um número inteiro: "))
    lista.append(numeros)
    
lista_ordenada = sorted(lista)
print(lista_ordenada)