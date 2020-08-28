tab = 9 
counter_1 = 0
counter_2 = 0
mult = 9

while counter_1 <= tab:
    while counter_2 <= tab:
        mult = counter_2 * counter_1
        print(f'{counter_1} x {counter_2} = {mult} | ', end='')
        counter_2 += 1
    print('')
    counter_2 = 0 
    counter_1 += 1