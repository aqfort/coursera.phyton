# print("hello")

print("---------")

a = 1_000_000
print(a, type(a))

a = 2.5_005
print(a)

a = "hello"
print(a)

print("---------")

a = 1.505e2
print(a, type(a))
a = int(a)
print(a, type(a))
a = float(a)
print(a, type(a))

print("---------")

for i in range(3):
  print(i)
  print(i + 1)

"""
kek
kek
kek
"""

print("---------")

a = 14 + 1j

print(type(a))
print(a.real, a.imag)

print("---------")

print(13 == 13.0)

a = 2
print(1 < a < 3)

print("---------")

print("3.14" in "PI = 3.1415926535")

print("---------")

income = None

if income is None:
  print("Not started selling yet")
elif not income:
  print("No income")

del income

print("---------")

a = 3
while a > 0:
  print(a)
  a -= 1

print("---------")

a = "Alex"

for char in a:
  print("Char: " + char)

print("---------")

pi = 3.1415926
pi_fmt = f"{pi:#0.2f}"

print(type(pi_fmt))

print("---------")
