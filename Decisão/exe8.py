#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

while True:
    prod1 = float(input("Digite o preço do primeiro produto: "))
    
    prod2 = float(input("Digite o preço do segundo produto: "))
    
    prod3 = float(input("Digite o preço do terceiro produto: "))
    

    if prod1 < prod2 and prod1 < prod3:
        print(f"Você deve comprar o produto 1, pelo valor de R${prod1}.")
        break
    elif prod2 < prod1 and prod2 < prod3:
        print(f"Você deve comprar o produto 2, pelo valor de R${prod2}.")
        break
    elif prod3 < prod1 and prod3 < prod2:
        print(f"Você deve comprar o produto 3, pelo valor de R${prod3}.")
        break
    else:
        print("Todos os produtos tem o mesmo preço, busque outros produtos.")