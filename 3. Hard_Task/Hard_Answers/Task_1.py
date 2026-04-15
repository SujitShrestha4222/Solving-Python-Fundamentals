nums = [2, 7, 11, 15]
target = 9


for i in range (len (nums)):            
    # print(i) gives output:0 1 2 3  
    # print(nums[i]) gives output:2 7 11 15          
    for j in range(i+1, len(nums)):              # when i=0 then 0+1=range(1,3) & when i=1 then 1+1=range(2,3) and so on... 
        # print(j) gives output:1 2 3, 2 3, 3  
        # print(nums[j]) gives output:7 11 15, 11 15, 15    
        if nums [i] + nums [j] == target:        # means 2+7==9 / 2+11==9 / 2+15==9 / 7+11==9 / 7+15==9 / 11+15==9
            print ([i, j])                       # since we want to index and not the values so...