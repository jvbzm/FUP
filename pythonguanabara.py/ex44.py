preço = float(input('Qual o valor do produto?:'))
pagamento = int(input('''Qual o modo de pagamento?'\n(1) para pagamento a vista em dinheiro ou cheque.\n(2) para pagamentoa vista no cartão.\n(3) para pagamento parcelado em até 2x no cartão.\n(4) para pagamento de 3x ou mais no cartão.
Qual você deseja?:'''))
if pagamento == 1:
    desc = preço*0.10
    print(f'O seu produto foi pago em dinheiro ou cheque à vista e terá o seu valor com 10% de desconto, sendo R${desc}')
elif pagamento == 2:
    desc = preço*0.05
    print(f'O seu produto foi pago à vista no cartão e terá 5% de desconto, sendo de R${desc}')
elif pagamento == 3:
    print(f'O seu produto foi pago em até 2x no cartão e terá o preço do anúncio, sendo de R${preço} ')
elif pagamento == 4:
    jr = preço*0.20 + preço
    parcel = int(input('Quantas parcelas você deseja?: '))
    parcela = jr/parcel
    parcela1 = round (parcela, 2)
    print(f'O seu produto foi parcelado em 3x ou mais, então será cobrado juros de 20% de acordo com a quantidade de parcelas. O valor do acréssimo é de R${parcela1}')
else:
    erro = 0
    print('Digite novamente!')