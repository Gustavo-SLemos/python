#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

def calculo_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calculo_fatorial(numero - 1)
    
while True:
    numero_usuario = int(input("Digite o número inteiro para o fatorial: "))

    if numero_usuario >= 0 and numero_usuario <=16:
        resultado = calculo_fatorial(numero_usuario)
        print(f"O fatorial de {numero_usuario}! é =", end = " ")
        for i in range(numero_usuario, 0, -1):
            print(i, end = " ")
            if i != 1:
                print(".", end = " ")
        print(f" = {resultado}")
    else:
        print("Valor inválido, tente novamente.")