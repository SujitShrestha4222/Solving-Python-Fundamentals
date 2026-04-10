num = int (input ("Enter a positive number:"))

while num <= 0:
    # Loop runs WHILE the number is NOT positive (<= 0)
    # As soon as the user enters a positive number (> 0),
    # If the condition is TRUE/ MET → the loop runs(goes inside the loop) & If the condition is FALSE / DIDN'T MET → the loop stops(don't go inside the loop) 
    # (E.g: if num = -5, loop runs & goes to inside asking input again) (E.g: if num = 2, loop stops without going inside)
    num = int (input ("Please enter a valid positive number: "))

print ("Thank you for response.")