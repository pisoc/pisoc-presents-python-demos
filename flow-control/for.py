"""for / else"""

will_break = False

# It's a for-each!
for i in range(5):
    print(i)
    if will_break and i == 3:
        break
else:
    print('We didn\'t break out of the loop')
