"""while / else"""

counter = 0
will_break = True

while counter < 5:
    print(counter)
    counter += 1

    if will_break and counter == 3:
        break
else:
    print('We didn\'t break out of the loop')
