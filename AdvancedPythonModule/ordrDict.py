d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4
d['e']=5
d['f']=6
d['g']=7

for k,v in d.items():
    print (k,v)

from collections import OrderedDict
d=OrderedDict()

d['a']=1
d['b']=2
d['c']=3
d['d']=4
d['e']=5
d['f']=6
d['g']=7

for k,v in d.items():
    print(k,v)
t1={}
t2={}

t1['a']=1
t2['b']=2
t2['b']=2
t1['a']=1

print(t1==t2)