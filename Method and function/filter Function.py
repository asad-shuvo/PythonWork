def check_even(num):
    return num%2==0

myList=[1,2,3,4,5,6,7,8]
for n in filter(check_even,myList):
    print(n)