lst = [1, 2, 3, 4, 5]
new_lst = []

for i in lst:
    if i % 2 == 0:
        new_lst. append (i ** 2)
    else:
        new_lst. append (i)

print (new_lst)





"""-----OR-----"""





lst1 = [12, 13, 14, 15]

for i in range (len (lst1)):         # means range is from 0 to 4 (basically becomes like index of lst)
    if lst1 [i] % 2 == 0:
        lst1 [i] = lst1 [i] ** 2     # or, lst[i] = lst [i] * lst[i]
        
print (lst1)