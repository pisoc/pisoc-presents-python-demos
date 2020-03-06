"""classes and objects"""


class OurClass:
    some_value = 10

    def __init__(self, other_value):
        self.other_value = other_value


# Works as expected
our_class = OurClass(20)
print(our_class.some_value)
print(our_class.other_value)
