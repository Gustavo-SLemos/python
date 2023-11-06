#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_do_quadrado = float(input("Digite o tamanho de um dos lados do quadrado: "))
area_do_quadrado = lado_do_quadrado * lado_do_quadrado

dobro = round((area_do_quadrado * 2), 2)

print(f"O dobro da área do quadrado é: {dobro}")