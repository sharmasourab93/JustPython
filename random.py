"""
Python: Using Random
"""


class NotSoRandom(object):

    def __init__(self):
        self.seed_val = int()

    def seed(self, a=3):
        self.seed_val = a

    def random(self):
        self.seed_val = self.seed_val * 3 % 19

        return self.seed_val


if __name__ == '__main__':
    _inst = NotSoRandom()
    seed = _inst.seed
    random = _inst.random

    seed(123)
    print([random() for _ in range(10)])