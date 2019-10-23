list1 = [1,2,3]
list1.append(4)

print(list1)
print(list1.count(10))
print(list1.count(1))
x = [1, 2, 3]
x.append([4, 5])
print(x)
x=[1,2,3]
x.extend([4,5])
print(x)
print(list1.index(2))
#print(list1.index(12))
list1.insert(2,'inserted')
print(list1)
ele=list1.pop()
print(ele)
print(list1)
list1.pop(2)
print(list1)
list1.append('Add')
print(list1)
list1.remove('Add')
print(list1)
list1.reverse()
list1.sort()

x=[1,2,3]
y=x.copy()
y.append(4)
print(x)
print(y)