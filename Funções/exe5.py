#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImposto(taxaImposto, custo):
    calculo_imposto = custo * taxaImposto
    valor_total = calculo_imposto + custo
    return valor_total

custo = float(input("Digite o custo antes do imposto: "))
taxaImposto = float(input("Digite a porcentagem de imposto em decimal: "))

valor_final = somaImposto(taxaImposto, custo)
print(valor_final)