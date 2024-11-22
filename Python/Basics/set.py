
d={1,2,3,4}

print(d.union([11,22,33]))
print(d)

f={1,2,3,4,5,6}
r= f.copy()
f.add(7)
print(f)
print(r)

a = {"osama","mazen",True,1,2}

#a.clear()
#print(a)
#b.remove(6)
#print(b)

#b.discard(6)
#print(b)

a.pop()
print(a)

c = {1,2,3,4,5}
b = {6,7,8,9,10}
c.update(b)
print(c)

print("="*50)
print("="*50)
print("="*50)




a2={1,2,3,4}
b2={1,2,"osama","ahmed"}
print(a2)
print(a2.difference(b2))
print(a2-b2)
print("=" * 40)

c2={1,2,3,4}
d2={1,2,"osama","ahmed"}

print(c2)
c2.difference_update(d2)
print(c2)

print("=" * 40)

e2={1,2,3,4,"x"}
f2={"osama","x",2}

print(e2)
print(e2 & f2)
print(e2.intersection(f2))


g2={1,2,3,4,"x"}
h2={"osama","x",2}

print(g2)
g2.intersection_update(h2)
print(g2)


i2={1,2,3,"x","mosua"}
j2={"x","ibrahim",1,2,}
print(i2)
print(i2.symmetric_difference(j2))
print(i2 ^ j2)
print(i2.difference(j2))
print(i2.intersection(j2))



r={1,2,3,"x","mosua"}
t={"x","ibrahim",1,2,}

print(r)
r.symmetric_difference_update(t)
print(r)


print("="*50)
print("="*50)
print("="*50)


a3={1,2,3,4}
b3={1,2,3}
c3={1,2,3,4,5}
print(a3.issuperset(b3))
print(a3.issuperset(c3))

print("="*40)

d3={1,2,3,4}
e3={1,2,3}
f3={1,2,3,4,5}

print(d3.issubset(e3))
print(d3.issubset(f3))

print("="*40)

g3={1,2,3,4}
h3={1,2,3}
i3={7,6,5}
print(g3.isdisjoint(h3))
print(g3.isdisjoint(i3))