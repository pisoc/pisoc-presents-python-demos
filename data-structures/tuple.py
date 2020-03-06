"""tuple"""

assorted_things = ('A string!', 1337, True)

for things in assorted_things:
    print(things)

# We can hash these...
print()
print('Hash:', hash(assorted_things), '\n')

# ..but not if it contains something mutable
print(hash(([1, 2, 3])))