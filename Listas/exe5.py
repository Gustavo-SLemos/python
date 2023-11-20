#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


def separar_par_impar(numeros):
    pares = []
    impares = []

    for numero in numeros:
        if numero %2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares

def main():
    lista = []

    for i in range(20):
        numero = int(input(f"Insira o {i + 1} número inteiro: "))
        lista.append(numero)

    lista_pares, lista_impares = separar_par_impar(lista)

    print("Lista completa: ", lista)
    print("Impares: ", lista_impares)
    print("Pares: ", lista_pares)

main()