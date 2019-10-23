'''
try:
    #for i in [1, 1, 3]:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("Woops Its not a number, so it cant be square, try with numeber")
else:
    print("Its number, so no problem")
finally:
    print("I will always print")
'''
'''
try:
    x = 5
    y = 0

    z = x / y
except ZeroDivisionError:
    print("Woops you can't divide a number with  zero")
else:
    print("All is good")
finally:
    print("All done")
'''
'''
'''
def ask():
    while True:
        try:
            inp=int(input("Please enter a number"))
        except:
            print("Please enter a number, its not a number")
            continue
        else:
            print(inp**2)
            print("Well done")
            break
        finally:
            print("All done")


ask()