#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_hora = float(input("Digite o valor hora do seu trabalho: "))
horas_trabalhadas = float(input("Digite quantas horas você trabalhou no mês: "))
total_bruto = ganho_hora * horas_trabalhadas
ir = round((total_bruto * (11/100)), 2)
inss = round(((total_bruto - ir) * (8/100)), 2)
sindicato = round(((total_bruto - ir - inss) * (5/100)), 2)
descontos = ir + inss + sindicato
salario_liquido = total_bruto - descontos

print(f"Salário Bruto: R${total_bruto} \nIR: RS${ir} \nINSS: RS${inss} \nSindicato: RS${sindicato} \nTotal do salário líquido: R${salario_liquido}")