from collections import Counter

l=[1,1,1,1,1,5,6,7,2,2,2,2,2,9,9]
print(Counter(l))

s="abaababjsjsasaksjlls"
print(Counter(s))

sw='This is s word word s s is is tree tree of life of'
words=sw.split()
print(Counter(words))
c=Counter(words)
print(c.most_common(2))
print(sum(c.values()))