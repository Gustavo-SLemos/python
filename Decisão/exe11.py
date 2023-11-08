#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario_atual = float(input("Digite seu salário atual: "))

if salario_atual <= 280:
    reajuste = salario_atual * 0.2
    print(f"O seu salário atual é de R${salario_atual}.")
    print(f"O seu percentual de aumento foi de 20%.")
    print(f"O valor do seu aumento foi de R${reajuste}.")
    print(f"O seu novo salário é de R${salario_atual + reajuste}.")
elif salario_atual > 280 and salario_atual < 700:
    reajuste = salario_atual * 0.15
    print(f"O seu salário atual é de R${salario_atual}.")
    print(f"O seu percentual de aumento foi de 15%.")
    print(f"O valor do seu aumento foi de R${reajuste}.")
    print(f"O seu novo salário é de R${salario_atual + reajuste}.")
elif salario_atual > 700 and salario_atual < 1500:
    reajuste = salario_atual * 0.1
    print(f"O seu salário atual é de R${salario_atual}.")
    print(f"O seu percentual de aumento foi de 10%.")
    print(f"O valor do seu aumento foi de R${reajuste}.")
    print(f"O seu novo salário é de R${salario_atual + reajuste}.")
else:
    reajuste = salario_atual * 0.05
    print(f"O seu salário atual é de R${salario_atual}.")
    print(f"O seu percentual de aumento foi de 5%.")
    print(f"O valor do seu aumento foi de R${reajuste}.")
    print(f"O seu novo salário é de R${salario_atual + reajuste}.")