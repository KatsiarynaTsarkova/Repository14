import random
#Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
#N может быть любой длины.
#N = 132 + 132132 + 132132132 = 132264396

number = random.randint(1, 999) 
print(number)
number = str(number)
number_f = number
number_s = number+number
number_t = number+number+number
result = int(number_f)+ int(number_s) + int(number_t) 
print(result)