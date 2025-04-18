prod = float(input('Qual o valor do produto?'))
desc = prod * 0.05
vf = prod - desc
print('O produto de valor R${} com desconto de 5%, vai passar a valer R${}'.format(prod,vf))