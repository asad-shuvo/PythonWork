def new_decorator(orginal_func):
    def wrap_funtion():
        print("Some extra code ,before the orginal one")
        orginal_func()

        print("Some extra code after the original function")

    return wrap_funtion

'''def func_needs_decorator():
    print("I want to be decorated")
decorated_func=new_decorator(func_needs_decorator)
decorated_func()'''
@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator()