#Importação da randon
import random

#Criação das vaiáveis.
numero = random.randint(0, 25)
tentativas = 1

#Loop para realizar tentativas de descobrir o número secreto.
while True:
    palpite = int(input("Digite seu palpite de 0 até 25 para o número oculto: "))
    if palpite == numero:
        print("Parabéns, você acertou o número oculto!")
        if tentativas >= 1 and tentativas <= 3:
            print(f"Você é muito sortudo, acertou em {tentativas} tentativas.")
        elif tentativas >= 4 and tentativas <= 6:
            print(f"Você é sortudo, acertou em {tentativas} tentativas.")
        elif tentativas >= 7 and tentativas <= 10:
            print(f"Normal, você acertou em {tentativas} tentativas.")
        else:
            print(f"Que azar, você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero:
        print("Tente um número maior.")
        tentativas += 1
    else:
        print("Tente um número menor.")
        tentativas += 1