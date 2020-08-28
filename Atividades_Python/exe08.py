list_numbers = []
numbers = int(input('Insira numeros [DIGITE 0 PARA ENCERRAR]: ')) 
b = numbers
s = numbers
while numbers != 0:
    list_numbers.append(numbers) 
    if numbers < s:
        s = numbers
    if numbers > b:
        b = numbers
    numbers = int(input('Insira numeros [DIGITE 0 PARA ENCERRAR]: '))
print(list_numbers)
print(f'O maior número é: {b}')
print(f'O menor número é: {s}')
