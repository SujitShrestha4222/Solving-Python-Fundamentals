a = "2.5"

# integer_a = int (a)        # cannot convert float like number string into integer directly
# print (integer_a)          # output: ERROR 
# print (type (integer_a))   # output: ERROR as we cannot directly convert string "2.5" into integer value

integer_a = int (float (a))  # firstly, converting to float ---> secondly, to integer value
print (integer_a)
print (type (integer_a))
