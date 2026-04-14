num = int (input ("Enter number:"))

original_num = num

armstrong_num = 0

power = len (str (num))    #converting to str type & using len() to know the length. REMEMBER THAT WITH CHANGE IN num WITH EVERY ITERATION, LENGTH ALSO CHANGES.


while num > 0:
    digit = num % 10
    armstrong_num = armstrong_num + digit**power
    num = num // 10
print ('total:', armstrong_num)

if original_num == armstrong_num:
    print ("is armstrong number.")
else:
    print ("not armstrong number.")