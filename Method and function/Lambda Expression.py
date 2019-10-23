square=lambda num:num**2
print(square(5))

myList=[1,2,3,4,5,6,7,8]

print(list(map(lambda num:num**2,myList)))

print(list(filter(lambda num:num%2==0,myList)))
myName=['andy','Debba','john']
print(list(map(lambda x:x[0],myName)))

print(list(map(lambda x:x[::-1],myName)))