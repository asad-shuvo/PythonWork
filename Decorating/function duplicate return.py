def hello(name="jose"):
    print("The Hello() Function Has been executed")

    def greet():
        return "\nThis is greet() function inside hello()"
    def welcome():
        return "\n this is welcome() inside hello()"

    print("I am going to return a function")

    if name=="jose":
        return greet
    else:
        return welcome

my_new_function=hello("jose")
print(my_new_function)
print(my_new_function())

def cool():
    def super_cool():
        return "I am super cool"
    return super_cool
my_fun_cool=cool()
print(my_fun_cool)
print(my_fun_cool())

'''
Passing the whole fuction, its super cool
'''

def hello():
    return "Hi Jose"
def other(some_other_function):
    print("Other code run here")
    print(some_other_function())
other(hello)