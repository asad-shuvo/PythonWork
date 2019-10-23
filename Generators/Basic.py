def create_cubes(n):
    for x in range(n):
        yield x**3
for x in create_cubes(10):
    print(x)

def gen_fib(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for i in gen_fib(10):
    print(i)
g=gen_fib(10)
print(next(g))
print(next(g))
print(next(g))

s="Hello its iterator"
s_iter=iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

