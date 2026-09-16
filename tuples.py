#tuples are immurable unliske lists which are mutable and any enty in the list can be changed at any time stoers ordered elements can be allowing duplicates ,faster and lightweight than lists
n=("hello","world")
print(type(n))
print(tuple("shreya"))
print(tuple([1,"shreya",2,3]))
print(n[0])
print(n[-1])
#n[0]="shreya"#error occurs 
#suppose you have to add "shreya in tuple n " create a tuple of shreya
print(n+("shreya",))
print(n)
print(n*3)
for i in n:
    print(i)
print("hello" in n)
print(min(n))
print(sorted((n),reverse=True))
print(n.count('hello'))
f=n
print(f)
#tuples are faster than lists
a,b,s,*others=(1,2,3,4,5,6,7)
print(a)
print(b)
print(s)
print(others)
g=(2,1,4,3)
print(g)
#ordred tuple means that each element has a fixed place