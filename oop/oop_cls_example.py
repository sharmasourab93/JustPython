"""
Python: Object Oriented Programming
        cls Method Example
"""


class Pizza:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return ' '.join(self.ingredients)

    @classmethod
    def margherita(cls):
        return cls(['mozarella', 'tomotoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozarella', 'tomatoes', 'ham'])


if __name__ == '__main__':
    print(Pizza.margherita())
    print(Pizza.prosciutto())