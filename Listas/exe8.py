#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

lista_idade = []
lista_altura = []

for i in range(2):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    lista_idade.append(idade)
    altura = float(input(f"Digite a altura da pessoa {i + 1}: "))
    lista_altura.append(altura)

lista_idade_inversa = list(reversed(lista_idade))
print(f"A lista inversa de idade é: {lista_idade_inversa}.")
lista_altura_inversa = list(reversed(lista_altura))
print(f"A lista inversa de altura é: {lista_altura_inversa}.")