#Exercise 2
vowels=('a', 'e', 'i', 'o', 'u')

#Normal way

def indexofelement(x,tuple):    
    for x in tuple:
        print(tuple.index(x))

indexofelement('a',vowels)

#Using comprehension

[print(x,vowels.index(x)) for x in vowels ]
[print(x,vowels.index(x)) for x in vowels if x =='a']