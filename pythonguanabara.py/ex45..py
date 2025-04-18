import random
jogada = int(input("Qual a sua jogada?:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nQual você escolhe?: "))
pc = random.randint(1,3)
print(f'A máquina escolheu {pc}')
if jogada == pc:
    print ("EMPATE!")
elif (jogada == 1 and pc == 2) or (jogada == 2 and pc == 3) or (jogada == 3 and pc == 1):
    print ("Você perdeu.")
else:
    print ("Você venceu!")