#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

sequencia = [1, 1]

def fibonacci(limite):
    while sequencia[-1] <= limite:
        sequencia.append(sequencia[-1] + sequencia[-2])

    return sequencia

#limite = int(input("Digite o valor limite da sequência de fibonacci: "))

resultado = fibonacci(500)

print(f"O resultado da sequência é {resultado}.")