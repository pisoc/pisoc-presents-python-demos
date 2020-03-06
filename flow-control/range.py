"""The range function"""

# Produces a range 0 to N
# Range is it's own type
some_range = range(10)
print(type(some_range))
print(list(some_range), '\n')

# Start and end points
some_range = range(10, 20)
print(list(some_range), '\n')

# Start and end points, and increment
some_range = range(20, 10, -2)
print(list(some_range), '\n')
