#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

numero = int(input("Digite um número inteiro: "))
if numero < 0:
    print("Número digitado negativo, tente novamente.")
else:
    resultado = fatorial(numero)
    print(f"O fatorial de {numero}! é: ", end="")
    for i in range(numero, 0, -1):
        print(i, end="")
        if i != 1:
            print(".", end="")
    print(f" = {resultado}")