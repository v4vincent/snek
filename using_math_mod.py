import math

# Assign point_dist with the distance between point (x1, y1) and point (x2, y2).

x1 = 1
y1 = 2
x2 = 1
y2 = 5

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f"{distance:.1f}")