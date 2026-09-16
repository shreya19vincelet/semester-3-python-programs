l1=[1,2,3]
print(id(l1))
print(id(l1[0]))
name="shreya"
print(list(name))
print((list(name))[-1])
l2=[1,2,3,[4,5]]
print(l2[-1][1])
l2[0]=100
print(l2)
l1.append(100)
print(l1)
l1.extend([500,600])
print(l1)
l1.insert(1,"world")
print(l1)
del l1[0]
print(l1)
l1.remove(2)
print(l1)
l1.pop()
print(l1)
l1.clear()
print(l1)
print(l1+l2)
print(l2*3)
print(1 in l2)
print(2 in l2)
for i in l2:
    print(i)