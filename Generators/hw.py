def gensqre(n):
    for x in range(n):
        yield x**2

for x in gensqre(10):
    print(x)
    
h="hello"
g=iter(h)
print(next(g))
print(next(g))
print(next(g))
