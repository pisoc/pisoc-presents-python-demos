"""keyword arguments"""

def very_complex_function(something, something_else, important, other):
    return '+'.join([something, something_else, important]) + other

# Who knows what this does?
# very_complex_function('a', 'b', 'c', 'd')

# Much clearer!
very_complex = very_complex_function(
    something='a',
    something_else='b',
    important='c',
    other='d'
)
print(very_complex)
