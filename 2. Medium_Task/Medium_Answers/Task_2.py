num = int (input ("Enter your number you want the reverse of:"))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit    # we need *10 as there is no such thing like concat with numbers(only addition)
    num = num // 10
print (rev)



"""
Code Execution Explaination:
Step-1: num = int (input ("Enter you number you want the reverse of:"))
        >>> We get an integer input from the user which is stored in the variable num.

Step-2: rev = 0
        >>> We create a variable called rev. It starts from 0 because we will build the 
            reversed number digit by digit. It means later on, we will be updating this 
            variable with new value.

Step-3: while num > 0:
        >>> This while loop runs as long as num is greater than 0. The loop helps us 
            process each digit of the number one by one.
            ---> IF THE CONDITION IS TRUE / MET = GOES INSIDE LOOP.
            ---> IF THE CONDITION IS FALSE / DIDN'T MET = LOOP STOPS AND GO OUTSIDE OF LOOP. 

Step-4: digit = num % 10
        >>> We know that % (modulus operator) gives us the remainder.
            num % 10 extracts the last digit of num. This remainder is stored in a variable 
            called digit.
            Example: if num = 436, then digit = 6 on first time looping
                                   then digit = 3 on second time looping
                                   then digit = 4 on third time looping

Step-5: rev = rev * 10 + digit
        >>> We shift the current value of rev one place to the left by multiplying it by 10,
            then we add the extracted digit to it. This is how the reversed number is formed 
            step by step.
            Example: from above example, we got digit = 6 from our first time looping. 
                        ---> rev = 0 * 10 + 6 ---> 0 + 6 ---> 6. Hence updated rev = 6
                     again, we got digit = 3 from our second time looping.
                        ---> rev = 6 * 10 + 3 ---> 60 + 3 ---> 63. Hence updated rev = 63
                     again, we got digit =  from our second time looping.
                        ---> rev = 63 * 10 + 4 ---> 630 + 4 ---> 63. Hence updated rev = 634

                    Therefore our rev = 634 which is the reversed our num variable value.
        >>> NOTE THAT YOU CAN ALSO DO (rev = digit + rev * 10) LIKE THIS AS HERE, WE ARE JUST
            ADDING THE INTEGER NUMBERS. SO, THE LOCATION ITSELF DON'T MATTER LIKE IN THE 
            QUESTIONS LIKE REVERSING STRINGS.

Step-6: num = num // 10
        >>> // 10 removes the last digit from num. we are dividing only to make sure our num
            changes everytime  as we know, if we don't do so, we get the iteration for 
            infinite time without any condition to stop the iteration.            
            This prepares num for the next loop iteration.                              
            Example: if num = 436 ,
                     from above example, in our first time looping. 
                        ---> num = 436 // 10 ---> 43. Hence updated num = 43
                     again, in our second time looping. 
                        ---> num = 43 // 10 ---> 4. Hence updated num = 4
                     from above example, in our first time looping. 
                        ---> num = 4 // 10 ---> 0. Hence updated num = 0
                     
                     Therefore, on each iteration, the value of num variable decreases and 
                     at last becomes 0.
                     DUE TO THIS, OUR CONDITION (while num > 0:) BECOMES FALSE AND THE LOOP 
                     STOPS.

Step-7: print (rev)
        >>> At last to print our rev variable value, we used print () function.
        >>> NOTE THAT WE HAVE USED PRINT() FUNCTION OUTSIDE OF THE LOOP AS WE DON'T WANT 
            TO PRINT ALL OF THE ITERATION VALUE OF LOOPING             
            INSTEAD, WANTED TO PRINT ONLY THE ACTUAL LAST VALUE  (FINAL OUTPUT) OF THE LOOP.
"""
