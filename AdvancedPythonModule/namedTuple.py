from collections import namedtuple
Cat =namedtuple('cat','age breed name')
sam=Cat(age=2,breed='Lovely',name='sammy')
tickle=Cat(age=3,name='tickle',breed='TT')
print(sam.name)
print(sam)
print(tickle.age)
print(tickle[0])