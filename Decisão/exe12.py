#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite quantas horas você trabalha por mês: "))
salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir = 0
    porcentagem = "Isento"
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    porcentagem = "5%"
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = salario_bruto * 0.1
    porcentagem = "10%"
else:
    ir = salario_bruto * 0.2
    porcentagem = "20%"

sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
inss = salario_bruto * 0.1

descontos = ir + sindicato + inss
salario_liquido = salario_bruto - descontos

print("------------------------------------------------")
print(f"Salário Bruto: R${salario_bruto} \n(-) IR ({porcentagem}): R${ir} \n(-) INSS (10%): R${inss} \n(-) Sindicato (3%): R${sindicato} \nFGTS (11%): R${fgts} \nTotal de descontos: R${descontos} \nSalário Líquido: R${salario_liquido}")