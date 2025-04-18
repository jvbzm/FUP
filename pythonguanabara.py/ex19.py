import random
al1 = input('Primeiro aluno é o(a): ')
al2 = input('Segundo aluno é o(a): ')
al3 = input('Terceiro aluno é o(a): ')
al4 = input('Quarto aluno é o(a): ')
lst = [al1,al2,al3,al4]
sorteado = random.choice(lst)
print('O aluno sorteado foi {}'.format(sorteado))