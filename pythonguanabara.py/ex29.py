velo = float(input('A quantos km/h o carro estava?'))
if velo >80:
    print('Sua velocidade excedeu o limite, você será multado!')
    multa = (velo-80) * 7
    print(f'Sua multa por condução perigosa será de R${multa}') 
else:
    print('Você está dentro dos limites de velocidade!')