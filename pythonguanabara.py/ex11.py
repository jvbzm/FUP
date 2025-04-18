import math
parede = float(input('Qual o tamanho da parede?'))
altura = float(input('Qual a altura da parede?'))
area = parede*altura
print('A parede tem {}x{} de dimensão e {} de área'.format(parede,altura,area))
tinta = area/2
print('A quantidade de tinta necessária para pintar a parede em litros é de {}L'.format(tinta))               