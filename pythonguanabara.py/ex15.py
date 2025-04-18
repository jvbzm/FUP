km = float(input('Qual a quantidade de km que o carro foi usado?'))
dias = float(input('Por quantos dias o carro foi alugado?'))
totald = dias*60
totalkm = km*0.15
vf= totald +totalkm
print('O carro percorreu {}km em {} dias, o valor final a se pagar pelo aluguel do carro é de {}'.format(km,dias,vf))