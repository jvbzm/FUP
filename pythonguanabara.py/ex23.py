num = int(input('Digite um número de 0 a 9999: '))
num_str = str(num).zfill(4)
print('Unidade {}'.format(num_str[3]))
print('Dezena {}'.format(num_str[2]))
print('Centena {}'.format(num_str[1]))
print('Milhar {}'.format(num_str[0]))

#também dá pra fazer desse jeito, mas eu aprendi a fazer substituindo o inteiro por string e quis testar, o comando .zfill eu vi em algum vídeo e também decidi testar
#num = int(input("Digite um número entre 0 e 9999: "))
#un = num % 10
#dez = num // 10 % 10
#cen = num // 100 % 10
#mil = num // 1000 % 10
#print("Unidade: {}".format(un))
#print("Dezena: {}".format(dez))
#print("Centena: {}".format(cen))
#print("Milhar: {}".format(mil))