"""inheritance"""

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    def caclulate_area(self):
        return 3.141592654 * (self.diameter / 2) ** 2

class Food:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def is_delicious(self):
        return 'cheese' and 'meat' in self.ingredients


class Pizza(Circle, Food):
    def __init__(self, diameter, toppings):
        self.diameter = diameter
        self.ingredients = ['meat', 'cheese', 'dough'] + toppings


pepperoni_pizza = Pizza(12, ['pepperoni'])
print(pepperoni_pizza.caclulate_area())
print(pepperoni_pizza.is_delicious())
