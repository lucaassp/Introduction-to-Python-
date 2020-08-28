list_numbers = []
numbers = int(input('Adicione numeros a lista: '))
while numbers != 0:
    list_numbers.append(numbers)
    numbers = int(input('Adicione numeros a lista: '))

c = 0
i = 0
n = int(input('Insira um numero e saiba quantas vezes ele se repete: '))
while i < len(list_numbers):
    i_list = list_numbers[i]
    i += 1
    if i_list == n:
        c += 1
if n not in list_numbers:
    print('O numero não esta na lista! ')
else:
    print(f'O numero {n} se repete {c} vezes!')
print(list_numbers)