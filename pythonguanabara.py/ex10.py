real = float(input('Quantos reais você tem na sua carteira? '))
dolar = 5.7
conv = real/dolar
print('Infelizmente o dólar está muito caro, então com seus {} reais, fazendo a conversão terá {:.2f} doláres'.format(real,conv))