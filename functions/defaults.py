"""defaults"""

def add(a, b=100):
    if b != 100:
        print(f'Given b: {b}')

    return a + b

print(add(1, 2), '\n')
print(add(1))
