#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def calculo_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calculo_fatorial(numero - 1)
    
numero_usuario = int(input("Digite o número inteiro para o fatorial: "))

if numero_usuario < 0:
    print("Valor inválido, tente novamente.")
else:
    resultado = calculo_fatorial(numero_usuario)
    print(f"O fatorial de {numero_usuario}! é =", end = " ")
    for i in range(numero_usuario, 0, -1):
        print(i, end = " ")
        if i != 1:
            print(".", end = " ")
    print(f" = {resultado}")