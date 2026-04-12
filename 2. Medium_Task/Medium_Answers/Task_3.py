num = int (input ("Enter your number you want the reverse of:"))

original_num = num         # we need to store our original num got from user as needed later on to compare

rev = 0

while num > 0:
    digit = num % 10
    rev =  digit + rev * 10 
    num = num // 10
print (rev)

if original_num == rev:
    print ("Is Palindrome.")
else:
    print ("Not Palindrome.")



"""
Code Execution Explaination:
Step-1: same as Task_2
        >>> BUT HERE, YOU NEED TO STORE YOUR num VARIABLE ELSEWHERE IN ANOTHER NEW VARIABLE 
            (Let's say original_num = num) BECAUSE DUE TO OUR (num = num // 10 block of code 
            inside of while loop). HENCE, OUR num VARIABLE WILL BE UPDATED AND BECOMES ZERO 
            AT THIRD TIME OF LOOPING(i.e num = 0) AND OUR LOOPS STOP TOO SINCE CONDITION 
            BECOMES FALSE(i.e CONDITION DIDN'T MET).

Step-2: same as Task_2

Step-3: same as Task_2

Step-4: same as Task_2

Step-5: same as Task_2

Step-6: same as Task_2

Step-7: same as Task_2 
        >>> THIS STEP IS OPTIONAL AS OUR QUESTION IS BASICALLY TO CHECK IF PALINDROME OR NOT, 
            RATHER THAN SHOWING THE REVERSE VALUE.

Step-8: if original_num == rev:
            print ("Is Palindrome.")
        else:
            print ("Not Palindrome.")
        >>> Now, we just need to use comparision operator (==) to compare our rev variable
            value with our original_num variable value. Using if else statement we print 
            the statement we want. 
            It means:
            ---> if condition is TRUE, then print ("Is Palindrome.")
            ---> if condition is FALSE, then print ("Not Palindrome.")
        >>> WE KNOW THAT original_num VARIABLE JUST ONLY CARRIES THE COPIED VALUE OF OUR 
            num VARAIBLE OF INITIAL STAGE (ACTUAL INPUT OF USER).
        >>> NOTE THAT THIS IF ELSE STATEMENT IS OUTSIDE OF THE LOOP.
"""