frase = str(input('Escreva uma frase: ')).strip().lower()
print(f'A letra "A" aparece {frase.count("a")} vezes')
print(f'A letra "A" aparece a primeira vez na posição {frase.find("a") + 1}')
print(f'A última letra "A" aparece na posição {frase.rfind("a") + 1}')