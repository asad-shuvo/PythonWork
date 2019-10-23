Str="This is an Example split it out start"

for word in Str.split():
    if(word[0]=='s' or word[0]=='S'):
        print(word)






for x in range(0,10):
    if(x%2==0):
        print(x)

myList=[x for x in range(1,50) if x%3==0]
print(myList)

for x in range(1,100):
    if(x%3==0 and x%5==0):
        print("FizzBuzz")
    elif(x%3==0):
        print("Fizz")
    elif(x%5==0):
        print("Buzz")


        for word in Str.split():
            if(len(word)%2==0):
                print("Even")

                myList=[word[0] for word in Str.split()]
                print(myList)