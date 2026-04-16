num = int (input ("Enter a number: "))

total = 0

for i in range (1, num):
    if num % i == 0:             
        total = total + i
        print (total)

if total == num:
    print ("Perfect number")
else:
    print ("Not a perfect number")

"""        
Let's say num = 6 
---> firstly, i = 1 ---> 6 % 1 == 0 (condition met) ---> total updated to 0 + 1 = 1
---> then, i = 2 ---> 6 % 2 == 0 (condition met) ---> total updated to 1 + 2 = 3
---> then, i = 3 ---> 6 % 3 == 0 (condition met) ---> total updated to 3 + 3 = 6 
Here total is equal with our input num. Therefore, it's a perfect number.
"""