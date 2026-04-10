st = "abcdefghijkl"

rev_st = ""

for i in st:
    rev_st = i + rev_st     #concatination occurs where each new string concat with old one by updating(pushes old ones to right side due to the (i + rev_st))
print (rev_st [::2])



"""
we cannot do (rev_st + i) as it will give same output. For E.g: if we do (rev_st + i), 
---> (i) Firstly, takes "a" and updates our (rev_st) variable i.e (rev_st + i ---> "" + "a" ---> "a")
---> However, when (i) takes the next one i.e "b" and updates our (rev_st) variable i.e (rev_st + i ---> "a" + "b" ---> "ab")
---> Similarly, when (i) takes the next one i.e "b" and updates our (rev_st) variable i.e (rev_st + i ---> "ab" + "c" ---> "abc")
---> And this goes on...
"""     





"""-----OR-----"""





st1 = "abcdefghijkl"
rev_st1 = st1 [::-1]
second_ch_skip_rev_st = rev_st1 [::2]
print (second_ch_skip_rev_st)
