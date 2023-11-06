#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

#Qual o peso?
#Qual o excesso?
#Se mais peso do que 50kg, paga 4 reais por kg excedente.
#Qual o valor da multa?
#Imprima os dados (Peso, peso em excesso, multa)

peso = float(input("Digite o peso total diário de peixes: "))
excesso = peso - 50

if excesso > 0:
    multa = (4 * excesso)
    multa_em_reais = f"{multa:.2f}"
    print(f"O peso total de peixe foi de {peso}kg, com excesso de {excesso}kg e multa a pagar de R${multa_em_reais}.")
else:
    print(f"O peso total de peixe foi de {peso}kg e está dentro do limite permitido.")