import math
co = float(input('O comprimento do cateto oposto é:'))
ca = float(input('O comprimento do cateto adjacente é:'))
hpt = math.hypot(co, ca)
print('O cateto oposto valia {}, o adjacente {} e a hipotenusa vale {:.2f}'.format(co,ca,hpt))