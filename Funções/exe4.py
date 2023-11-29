#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def positivoNegativo(numero):
    if numero > 0:
        return "P - Positivo"
    else:
        return "N - Negativo"

numero = int(input("Digite um número positivo ou negativo: "))
resultado = positivoNegativo(numero)

print(f"O número digitado é {resultado}")