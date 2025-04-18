soma = 0
for num in range(0, 501, 3):
    print(num)
    if num % 3 == 0:
        soma += num
print(f'A soma total de todos os números ímpares e múltiplos de 3 é {soma}')