lst = [1, 2, 4, 6, 10]

missing_in_lst = []

for i in range ( (lst[1]), (lst[-1]+1) ):       # Using lst[1] to get first value lst[-1] to get last value of list then plus 1 as for loop excludes given last value
    if i not in lst:
        missing_in_lst. append (i)

# Viewing the missing_in_lst list
print (missing_in_lst)