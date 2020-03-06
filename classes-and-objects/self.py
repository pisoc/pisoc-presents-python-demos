"""self"""

class OurClass:
    some_value = 10

    def __init__(self, other_value):
        self.other_value = other_value

    # It's called self by convention
    def get_self_id(self):
        return id(self)

    @classmethod
    def get_class_id(cls):
        return id(cls)


# Works as expected
our_class = OurClass(20)
print(id(our_class) == our_class.get_self_id())
print(id(OurClass) == our_class.get_class_id())