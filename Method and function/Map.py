'''
def square(num):
    return num**2

my_nums=[1,2,3,4,5]

for items in map(square,my_nums):
    print(items)

lxt=list(map(square,my_nums)) #we can list the item of map
print(lxt)
'''
def stringOddEven(myString):
        if len(myString)%2==0:
            return 'Even '+myString
        else:
            return 'Odd '+myString




myname=['Andy','Buffe','Tand','Tera']
for item in map(stringOddEven,myname):
    print(item)
