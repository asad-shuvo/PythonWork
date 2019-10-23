d={'k1':1,'k2':2}
print({x:x**2 for x in range(10)})
d = {'k1':1,'k2':2}
for k in d.keys():
    print(k)
for k in d.values():
    print(k)
for k in d.items():
    print(k)
key_view = d.keys()

print(key_view)