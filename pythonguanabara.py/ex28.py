import random
prob = [0,1,2,3,4,5]
certo = random.choice(prob)
print('Escolha um número de 0 a 5 e te direi se você acertou qual número eu escolhi')
tentativa = int(input('Agora, escolha seu número de 0 a 5...'))
if tentativa == certo:
    print(f'Você acertou! O número é {certo}')
else:
    print(f'Você errou, o número escolhido foi o {certo} :(')