"""cool features"""

# Unpacking
a = 10
b = 20
l = [a, b]
x, y = l

print(l)
print(f'x: {x}, y: {y}\n')

# Comprehension
squares = [x ** 2 for x in range(1, 6)]
roots_and_squares = {x: x ** 2 for x in range(1, 6)}

print(squares)
print(roots_and_squares)
