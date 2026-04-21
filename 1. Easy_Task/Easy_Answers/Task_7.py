nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        break
else:
     print ("Loop completed!!!")

"""
Output: No output
Because:
- The else block we wrote is outside of for loop(not inside of for loop).
- The codition to run else block of a for loop is ---> when the loop get executed normally (i.e.without break).
However,
- Here, the loop stops early when num == 3, so the else block is skipped.
"""
# Example when else block is exectued and we get output: Loop completed!!!
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 9:
#         break
# else:
#      print ("Loop completed!!!")
