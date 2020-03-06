"""class / instance variables"""

class OurClass:
    class_var = 10

    def __init__(self, other_value):
        self.ints_var = other_value


# Works as expected
x = OurClass(20)
y = OurClass(30)
print(x.ints_var, y.ints_var, sep=', ')
print(x.class_var, y.class_var, sep=', ')

# Gotcha!
# OurClass.class_var = "qwerty"
x.class_var = "qwerty"
print(id(x.class_var) == id(y.class_var))
