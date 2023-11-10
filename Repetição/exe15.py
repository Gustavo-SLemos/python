#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

def fibonacci(n):
    sequencia = [1, 1]

    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])

    return sequencia[:n]

n = int(input("Digite o enésimo número para a sequência: "))

resultado = fibonacci(n)

print(f"O resultado da sequência é {resultado}.")