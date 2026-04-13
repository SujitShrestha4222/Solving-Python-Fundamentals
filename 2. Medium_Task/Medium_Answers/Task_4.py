num = int (input ("Enter your number:"))

total = 0

while num > 0:
    digit = num % 10
    total = total + digit    # Just adding the looping number of digit with total
    num = num // 10
print(total)