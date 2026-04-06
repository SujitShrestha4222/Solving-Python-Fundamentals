lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_of_even = 0       # since, we need addition of numbers so making variable of int for collecting even
sum_of_odd = 0        # since, we need addition of numbers so making variable of int for collecting odd

for i in lst:
    if i % 2 == 0:
        sum_of_even += i              # or, sum_of_even = sum_of_even + i
    else:
        sum_of_odd += i               # or, sum_of_odd = sum_of_odd + i

difference = sum_of_even - sum_of_odd
print (difference)