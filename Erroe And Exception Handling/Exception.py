try:
    result=10+'10'
except:
    print("Hey it looks like you aren't adding correctly")
else:
    print("It Gone well")
    print(result)

try:
    f=open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("Hey You Have an OSError")
finally:
    print("I always run")

def ask_for_int():
    while True:
        try:
            result=int(input("Please provide a number "))
        except:
            print("Woops its not a number")
            continue
        else:
            print("Yes Thank You")
            break
        finally:
            print("End of try/except/finally")
            print("I will always print")
ask_for_int()