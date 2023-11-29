#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def argumentos(one, two, three):
    resultado = one + two + three
    return resultado

one = int(input("Digite um número: "))
two = int(input("Digite um número: "))
three = int(input("Digite um número: "))

resultado_soma = argumentos(one, two, three)
print(resultado_soma)