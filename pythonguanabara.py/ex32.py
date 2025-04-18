ano = int(input('Qual ano deseja ver se é bissexto?'))
if ano % 4==0 and ano%100 !=0 or ano%400 ==0:
    print(f'{ano} é bissexto!')
else:
    print(f'{ano} não é bissexto')
##esse eu tive que ir buscar ajuda pra entender porque alguns anos que n eram bissextos estavam dando como bissesto