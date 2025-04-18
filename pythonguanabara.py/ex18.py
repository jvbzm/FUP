import math
ang = float(input('Qual ângulo você quer converter? '))
sen = math.sin(math.radians(ang))
print('O ângulo de {} é equivalente ao seno de {:.2f}'.format(ang,sen))
cos = math.cos(math.radians(ang))
print('O ângulo de {} é equivalente ao cosseno de {:.2f}'.format(ang,cos))
tg = math.tan(math.radians(ang))
print('O ângulo de {} é equivalente a tangente de {:.2f}'.format(ang,tg))