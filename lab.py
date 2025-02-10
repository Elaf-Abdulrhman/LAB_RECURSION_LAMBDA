# LAB_RECURSION_LAMBDA

## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4` 


vowels_counter = lambda word: 0 if word == '' else (1 if word[0].lower() in 'aeiou' else 0) + vowels_counter(word[1:])
print(vowels_counter('I love python')) # 4