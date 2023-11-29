def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print("Achei a chave!")

def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i - 1)

i = int(input("Digite um número para iniciar a contagem regressiva: "))
contagem  = regressiva(i)
print(contagem)