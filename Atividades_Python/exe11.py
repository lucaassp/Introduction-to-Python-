
list_odd_numbers = []
number_final = int(input('Digite o número: '))
i = 0
while i <= number_final:
    if i % 2 == 1:
        list_odd_numbers.append(i)
    i += 1
print(list_odd_numbers)
   