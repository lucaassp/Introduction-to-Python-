list_numbers = []
numbers = input('Insira numeros [DIGITE 0 PARA ENCERRAR]: ') 
while numbers != '0':
    list_numbers.append(numbers)
    numbers = input('Insira numeros [DIGITE 0 PARA ENCERRAR]: ') 
print(list_numbers)
