'''
#task 1
def vol(rad):
    return (4/3)*(3.14)*(rad**3)

print(vol(5))
'''
'''
#task 2
def ran_check(num,low,high):
    if num>=low and num<=high:
        return True
    else:
        return False

print(ran_check(5,3,7))
print(ran_check(4,3,7))
print(ran_check(2,3,7))
'''
'''
#task 3
def up_low(s):
    up=0
    low=0
    for i in range(0,len(s)):
        print(s[i])

        if s[i]>='A' and s[i]<='Z':
            up+=1
        if s[i]>='a' and s[i]<='z':
            low+=1
    print(up)
    print(low)
up_low('Hello')
'''
'''
#task 4
def unique_lisy(myList):
    return set(myList)
myList=[1,2,3,4,5,6,1,1,2,2]
print(unique_lisy(myList))
'''
'''
#task 5
def multiply(number):
    sum=1
    for i in range(0,len(number)):
        sum=sum*number[i]
    print(sum)


myList = [1,2,3,-4]
multiply(myList)
'''
'''
#task 6
def palindrome(s):
    rev=""
    rev=s[::-1]
    flag=0
    for i in range(0,len(s)):
        if s[i]!=rev[i]:
            flag=1
    if flag==0:
        print("Yes")
    else:
        print("No")
palindrome("hello")
palindrome("adoda")
palindrome("AdA")
'''
'''
#task 7
'''

def check(str1,str):
    print(set(str))
    return len(set(str))==4



str1="HELLo"
str=str1.lower()
print(str)

print(check(str1,str))
