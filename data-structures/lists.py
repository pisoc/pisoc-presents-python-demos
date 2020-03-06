"""lists"""

assorted_things = ['A string!', 1337, 3.141, True, [1, 2, 3]]

for things in assorted_things:
    print(things)

# It's the same number
print()
print(id(assorted_things))

assorted_things.append('Another string!')
print(assorted_things)

print(id(assorted_things), '\n')

# No hashing here!
print(hash(assorted_things))
