li = [4,5,6,7]
print(tuple(li))

[print(tuple(li)) for x in li]

lin = ['Hola', 'mundo', 'cruel']

[print(a[::-1]) for a in lin]

[print(x*y) for x in lin for y in li if x[-1]=='a']