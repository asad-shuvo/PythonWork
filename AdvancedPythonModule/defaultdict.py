from collections import defaultdict

d=defaultdict(object)
d=['one']

for item in d:
    print(item)

lmb=defaultdict(lambda :0)
lmb['one']
lmb['two']=2
print(lmb['one'])
print(lmb['two'])