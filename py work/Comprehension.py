str='helloWorld'

res = [letter for letter in str]

print(res)

myList=[num for num in range(0,10)]

print(myList)

myList=[num for num in range(0,10) if num%2==0]

print(myList)

myList=[num**2 for num in range(0,10) if num%2==0]

print(myList)

myList=[num if num%2==0 else 'ODD' for num in range(0,10)]
print(myList)

pth=[1,2,3]
far=[((9/5)*t+32) for t in pth]
print(far)

#nested loop

Lst=[x*y for x in [1,2,3] for y in [10,100,1000] ]

print(Lst)





