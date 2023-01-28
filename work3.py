#Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, 
# знаменатель которых не превышает 11.
def c_numbers(numerator, denominator):
    min_number = min(numerator, denominator)
    divider = 1
    for el in range(2, min_number+1):
        if numerator % el == 0 and denominator % el == 0:
           divider = el
           break
    return divider == 1   
for numerator in range(1, 12):
    for denominator in range(1, 12):
        if c_numbers(numerator, denominator):
           print(f'{numerator}/{denominator}', end =' ')