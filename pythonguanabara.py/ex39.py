from datetime import date
agora = date.today().year
idade = int(input('Qual a sua idade?: '))
nasc = agora - idade
anoalist = nasc + 18
if idade < 18:
    falta = 18 - idade
    print(f'Você ainda não está permitido para o alistamento militar, volte em {falta} anos.')
elif agora == anoalist:
    print('Está na hora de se alistar, você tem 18 anos.')
else:
    atraso = agora - anoalist
    print(f'Você está atrasado em {atraso} anos do ano de seu alistamento!')