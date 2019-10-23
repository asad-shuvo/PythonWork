'''
#Test 1
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    elif a%2==1 or b%2==1:
        return max(a,b)

print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))
'''

'''
# Test#2


def animal_crackers(text):
    list=text.split()
    return list[0][0]==list[1][0]
      
print(animal_crackers('Bordr Bd'))
print(animal_crackers('Bordr Id'))
'''

'''
#Task 3

def makes_twenty(n1,n2):
    if n1==20 or n2==20:
        return True
    elif n1+n2==20:
        return True
    else:
        return False


print(makes_twenty(20,10))
print(makes_twenty(20,11))
print(makes_twenty(11,11))
print(makes_twenty(19,1))
'''

'''
#task 4


def old_macdonald(str):
    st=str[0]
    st=st.upper()
    st=st+str[1:3]
    s=str[3]
    s=s.upper()
    st=st+s
    st=st+str[4:]
    print(st)
old_macdonald('macdonald')
'''
'''
#task #5


def master_yoda(text):
    myList=text.split()
    myList.reverse()
    str=""
    for x in myList:
        str=str+' '+x

    print(myList)
    print(str)

master_yoda("This is it")
master_yoda('I am home')
master_yoda('We are ready')
'''
'''
#task #6
def almost_there(n):
    if (abs(n-100)<=10) or(abs(n-200)<=10):
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
'''

'''
#task #7


def has_33(nums):
    for n in range(0, len(nums) - 1):
        if nums[n]==3 and nums[n+1]==3:
            return True





       # return False

t=has_33([1,3,1,4,5,3,1])
if(t!=True):
    print("False")
else:
    print("True")
'''
'''
#Task#8
def paper_doll(text):
    str=""
    for i in text:
        str+=i*3

    return str


print(paper_doll('hello'))
'''
'''
#task#9


def blackjack(a,b,c):
   if a+b+c<=21:
       return True
   elif 11 in (a,b,c):
       return True
   else:
       return 'Bust'


print(blackjack(9,9,9))
print(blackjack(5,6,7))
print(blackjack(9,9,11))
'''
'''
#task #10
def summer_69(arr):
    totla=0
    TheBol =True
    for x in arr:
        if TheBol==True and x!=6 and x!=9:
            totla+=x
        if x==6:
            TheBol=False
        elif x==9:
            TheBol=True
            continue
    return totla

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

'''
'''
#task # 11


def spy_game(nums):
  lxt=[0,0,7,'x']
  for x in nums:
      if x == lxt[0]:
          lxt.pop(0)
          print(len(lxt))

  return len(lxt)==1

print(spy_game([1,2,4,0,0,7,5]))
'''
'''
#task# 12
'''
def chk(num):
    flag=False
    for i in range(2,num-1):
            if num%i==0:
              flag=True


    if flag==False:
                return True
    else:
        return False

def cnt_prime(num):
    cnt=0
    for i in range(2,num):
        t=chk(i)
        if t==True:
            cnt=cnt+1


    return cnt

print(cnt_prime(10))





