#args usualy return as tuple ,you can pass as many parameter as possible
def myfun(*args):
    print(args)
    return sum(args)

print(myfun(1,2,3,4))

#kwargs

def myfun2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('the fruit in the dictionary is {}'.format(kwargs['fruit']))
    if 'veggi' in kwargs:
        print('The Veggi in the dictionary is {}'.format(kwargs['veggi']))

myfun2(fruit='Appale',veggi='lettuce')

#combination of args and kwargs

def myfun3(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i would like to bought {} {}'.format(args[0],kwargs['food']))

myfun3(1,2,3,4,food="Fish",meat="Mutton")


