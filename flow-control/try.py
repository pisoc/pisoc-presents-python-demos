"""try / except / else / finally"""


def something_dangerous():
    """Don't try this at home"""
    raise RuntimeError('Dangerous!')

feeling_lucky = True

# Won't catch exceptions that RuntimeError doesn't inherit from
try:
    if feeling_lucky:
        something_dangerous()
except RuntimeError as ex:
    print(f'Caught an error: {ex}')
else:
    print('Nothing went wrong... that\'s new!')
finally:
    print('This will be called regardless of failure')
