
def function_name(name,num):
    print('Hello '+name)
    print(num)



function_name('name',34)

#help(function_name)


def check(str):
    if 'dd' in str:
        return True
    else:
        return False

ret = check('dd in it')
print(ret)