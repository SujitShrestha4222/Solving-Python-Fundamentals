st = "python is easy"

st_without_whitespace = st. replace(" ","")
print (st_without_whitespace)                        # output: pythoniseasy

vowels = "aeiou"

vowels_count = 0
consonants_count = 0

for i in st_without_whitespace:
    if i in vowels:
        vowels_count = vowels_count + 1               # or, vowels_count += 1
    else:
        consonants_count = consonants_count + 1       #or, consonants_count += 1

print (f"The vowels count is {vowels_count}.\nThe consonants count is {consonants_count}.")