import sys

n = int(sys.argv[1])

for i in range(n,0,-1):
    print(" " * (i - 1) + "#" * (n - i + 1))

# import sys

# num_steps = int(sys.argv[1])

# for i in range(num_steps):
#     print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")
