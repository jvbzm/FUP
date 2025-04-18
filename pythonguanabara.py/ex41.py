idade = int(input('Qual a sua idade? '))
if idade < 10:
    print(f'Você tem {idade} anos e está na categoria: MIRIM')
elif idade <15:
    print(f'Você tem {idade} anos e está na categoria: INFANTIL')
elif idade <20:
    print(f'Você tem {idade} anos e está na categoria: JUNIOR')
elif idade == 20:
    print(f'Você tem {idade} anos e está na categoria: SÊNIOR')
else:
    print(f'Você tem {idade} anos e está na categoria: MASTER')