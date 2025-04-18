sal = float(input('Qual o salário do funcionário?'))
if sal >1250:
    sal10 = sal*0.10 + sal
    print(f'o novo salário com reajuste de 10% é de R${sal10}')
else:
    sal15 = sal*0.15 + sal
    print(f'O salário com reajuste de 15% é de R${sal15}')