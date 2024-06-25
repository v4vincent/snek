# float_num = float(input("Tell me a float: "))

# print(float_num)
import math

x = 15
y = 5
y = 5.4e8
print(y)


def avg_sales(num_sales1, num_sales2, num_sales3):
    ave = (num_sales1 + num_sales2 + num_sales3) / 3
    print(f"{ave:.2f}")


avg_sales(3, 4, 8)

pi = 3.14159
sphere_radius = float(input())
sphere_volume = (4.0 / 3.0) * (pi * sphere_radius ** 3)
print(f'Sphere volume: {sphere_volume:.2f}')


G = 6.673e-11
M = 5.98e24

dist_center = float(input())

accel_gravity = (G * M) / (dist_center**2)


print(f'Acceleration of gravity: {accel_gravity:.2f}')