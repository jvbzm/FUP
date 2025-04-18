valc = float(input('Qual o valor da casa que você deseja financiar?:'))
sal = float(input('Qual o seu salário?:'))
tempo = float(input('Em quanto meses você deseja parcelar?:'))
prest = valc/tempo
if prest*0.3 > sal:
    print(prest)
    print('O seu salário não corresponde para o seu plano desejado de financiamento, favor escolher outro plano.')
else:
    print(prest)
    print('O seu financiamento está de acordo!')