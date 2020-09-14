import sys

digit_string = sys.argv[1]

result = 0

for symbol in digit_string:
    result += int(symbol)

print(result)

# import sys

# print(sum([int(x) for x in sys.argv[1]]))
