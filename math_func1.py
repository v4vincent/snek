import math as mathematics

x = float(input())
y = float(input())
z = float(input())

your_value1 = mathematics.pow(x,z)
your_value2 = mathematics.pow(x,mathematics.pow(y,z))
your_value3 = abs(x - y)
your_value4 = mathematics.sqrt(mathematics.pow(x,z))

print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')