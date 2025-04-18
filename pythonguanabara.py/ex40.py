m1 = float(input('Qual a primeira nota desse aluno? '))
m2 = float(input('Qual a primeira nota desse aluno? '))
soma = m1 + m2
media = soma/2
if media < 5.0:
    print(f'Você está abaixo da nota miníma que é 5.0 e não tem direito a recuperação, sua nota é {media} e está reprovado.')
elif media < 6.9:
    print(f'Sua nota não foi suficiente para ser aprovado, porém está de recuperação, sua nota foi {media}')
else:
    print(f'Você foi aprovado! Sua nota foi {media}, parabéns')