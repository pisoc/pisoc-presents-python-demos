"""dicts"""

assorted_things = {
    'an_album': 'Zweihander - Forbidden Magic',
    'quake_release_year': 1996,
    'pisoc_is_cool': True
}

# indexing, .get. and it's default option
print(
    assorted_things.get('quake_release_year')
    == assorted_things['quake_release_year']
)
print(assorted_things.get('No key here!', 'No value either!'), '\n')

for key, value in assorted_things.items():
    print(f'{key} | {value}')

print()
fail_dict = {[]: 'Oh no!'}
