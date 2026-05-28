if "False":
    print ("Logic")
else:
    print ("No Logic")


# Output: Logic
"""
Code Explaination:
"False" we used is a non-empty string. 
In Python, any non-empty string is truthy — it doesn't matter what the string says, only whether it has content or not.

Example:
pythonbool("False")         # True  ← non-empty string
bool("True")                # True  ← non-empty string
bool("")                    # False ← empty string
So, 
"False" (the string) being truthy has nothing to do with it being "a string with nothing." It's truthy because it has characters in it.

A cleaner way to explain it:
"False" is a non-empty string, so Python evaluates it as True. The if block runs, printing "Logic".

NOTE: The only string Python treats as false is "" (an empty string).
"""