#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

# - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

while True:

    print("Menu:")
    print("Opção 1 para iniciar o programa.")
    print("Opção 2 para sair.")
    menu = int(input("Digite a opção escolhida: "))

    if menu == 1:

        pais_a = int(input("Digite a população do país 1 (menor): "))
        taxa_a = float(input("digite a taxa de crescimento anual da população no país 1: "))
        pais_b = int(input("Digite a população do país 2 (maior): "))
        taxa_b = float(input("digite a taxa de crescimento anual da população no país 2: "))
        ano = 0

        while pais_a < pais_b:
            pais_a += pais_a * taxa_a
            pais_b += pais_b * taxa_b
            ano += 1

        print(f"O País 1 levará {ano} anos até ultrapassar a população do país 2")

    else:
        print("Até mais!")
        break