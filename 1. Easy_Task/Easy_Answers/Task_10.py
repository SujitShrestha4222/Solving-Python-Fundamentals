st = "a1b2c3d4"

num_st = "0123456789"      # creating a variable consisting all numbers in string
total_sum_digit = 0        # creating an empty integer variable

for i in st:
    if i in num_st:
        int_i = int (i)                            # converting i's iterated string value to integer value
        total_sum_digit = total_sum_digit + int_i

print (total_sum_digit)