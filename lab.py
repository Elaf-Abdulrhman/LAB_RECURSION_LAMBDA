# LAB_RECURSION_LAMBDA

## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4` 


vowels_counter = lambda word: 0 if word == '' else (1 if word[0].lower() in 'aeiou' else 0) + vowels_counter(word[1:])
print(vowels_counter('I love python')) # 4

## 2) Given a list of numbers : `[40,35, 10, 15, 20]`

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Note: use `map()` with a `lambda funciton`

numbers = [40,35, 10, 15, 20]
new_list = list(map(lambda x: x*x, numbers)) #The map function applies a given function to each item of an iterable
print(new_list) 