def fibonacci(n):

    sequencia = [1, 1]

    while len(sequencia) < n:
        novo_termo = sequencia[-1] + sequencia[-2]
        sequencia.append(novo_termo)
    
    return sequencia

n = int(input("Digite o n-ésimo número da sequencia: "))
resultado = fibonacci(n)

print(f"A sequência fibonacci é: {resultado}")