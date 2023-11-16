#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def consoantes(vetor):
    consoantes = 0
    lista_consoantes = []

    for char in vetor:
        if char.isalpha() and char.lower() not in "aeiou":
            consoantes += 1
            lista_consoantes.append(char)
    
    return consoantes, lista_consoantes

vetor = input("Digite algo com 10 caracteres: ")[:10]

total_consoantes, lista_consoantes = consoantes(vetor)

print(f"Total de consoantes: {total_consoantes}")
print("Consoantes:", ', '.join(lista_consoantes))