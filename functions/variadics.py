"""variadic arguments"""

# Sums all positional arguments
def our_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# Displays what kw/args we got
def prints_things(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs.get('key'))

# So many arguments!
print(our_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), '\n')

# Variadics and unpacking
prints_things(
    *(1, 2, 3),
    **{'key': 'value'}
)
