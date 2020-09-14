import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b * b - 4 * a * c

x_1 = int((-b - math.sqrt(D)) / (2 * a))
x_2 = int((-b + math.sqrt(D)) / (2 * a))

print(x_1)
print(x_2)
