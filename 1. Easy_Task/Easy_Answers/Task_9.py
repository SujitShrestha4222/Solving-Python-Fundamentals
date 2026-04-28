lst = [1, 2, 3, 4, 5]
new_lst = []

for i in lst:
    if i % 2 == 0:
        new_lst. append (i)
    else:
        new_lst. append (0)

print (new_lst)

"""-----OR-----"""

# suppose you just want to update the existing list itself(lst1), then:
lst1 = [1, 2, 3, 4, 5]

for i in range (len(lst1)):   # means range is from 0 to 4 (basically becomes like index of lst)
    if lst1[i] % 2 != 0:
        lst1[i] = 0

print (lst1)

