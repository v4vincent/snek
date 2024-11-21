x = [1,2,3]
y = [1,2,3]

if x is y:
    print("same object")
else:
    print("different objects")

if x == y:
    print("same values")
else:
    print("different values")

print(f"{id(x)}\n{id(y)}")

x = 500
y = x + 250

if x is y:
    print("true")
else:
    print("false")

print(f"{id(x)}\n{id(y)}")

a = 1
b = 2
c = [a, b]

print(id(c[0]))
print(id(a))