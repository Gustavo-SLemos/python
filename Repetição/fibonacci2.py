#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

def fibonacci(n):
    sequencia = [1, 1]
    while len(sequencia) < n:
        novo_elemento = sequencia[-1] + sequencia[-2]
        sequencia.append(novo_elemento)
    return sequencia

n = int(input("Digite um número para a sequência fibonacci: "))
resultado = fibonacci(n)

print(f"A sequência fibonacci é: {resultado}")