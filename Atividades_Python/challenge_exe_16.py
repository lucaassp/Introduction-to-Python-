list_numbers = []
numbers = int(input('Digite numeros a lista [DIGITE 0 PARA ENCERRAR]: '))
while numbers != 0:
    
    for i, v in enumerate(list_numbers):
        if numbers < v:
            list_numbers.insert(i, numbers)
            break
    else:
        list_numbers.append(numbers)
    numbers = int(input('Digite numeros a lista [DIGITE 0 PARA ENCERRAR]: '))
print(list_numbers)