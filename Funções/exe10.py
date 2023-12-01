#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def jogaDados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def craps():
    primeira_jogada = jogaDados()

    if  primeira_jogada == 7 or primeira_jogada == 11:
        print(f"Seu resultado foi {primeira_jogada} - Natural - você ganhou!")
    
    elif primeira_jogada == 2 or primeira_jogada == 3 or primeira_jogada == 12:
        print(f"Seu resultado foi {primeira_jogada} - Craps - você predeu!")
    
    else:
        print(f"{primeira_jogada} é seu Ponto")
        ponto = primeira_jogada
    
        while True:
            nova_jogada = jogaDados()
            if nova_jogada == ponto:
                print(f"Você tirou o mesmo número {ponto}, você venceu!")
                break
            elif nova_jogada == 7:
                print(f"Você tirou 7 e perdeu!")
                break
            else:
                print(f"Você tirou {nova_jogada}, continue tentando!")

craps()