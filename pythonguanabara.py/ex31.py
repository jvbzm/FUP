viag = float(input('Qual a distância da viagem?'))
preço = viag * 0.5
if viag >200:
    preço = viag * 0.45
    print(f'Sua viagem excede 200km, então o preço dela é de R${preço}')
else:
    print(f'Sua viagem de {viag}km custa R${preço}')