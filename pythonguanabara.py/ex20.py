import random
al1 = input('Primeiro aluno é o(a): ')
al2 = input('Segundo aluno é o(a): ')
al3 = input('Terceiro aluno é o(a): ')
al4 = input('Quarto aluno é o(a): ')
lst = [al1,al2,al3,al4]
random.shuffle(lst)
print('A ordem da lista é: {}'.format(lst))