import math
altura = float(input('Qual a sua altura?: '))
peso = float(input('Qual o seu peso?: '))
imc = peso / math.pow(altura, 2)
imc3 = round (imc, 1)
if imc <18.5:
    print(f'O seu IMC é {imc3} e está abaixo do peso.')
elif imc < 25:
    print(f'O seu IMC é {imc3}. Você está no peso ideal')
elif imc < 30:
    print(f'O seu IMC é {imc3} e você ultrapassa os 25, significa que está com sobrepeso')
elif imc < 40:
    print(f'O seu IMC é {imc3} e a partir de 30 siginifca que está com obesidade.')
else:
    print(f'O seu IMC é {imc3}, acima de 40 significa que é uma obesidade mórbida.')