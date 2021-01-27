"""
Python: Pytest
        Learning Pytest with Examples
        Example 2: Mocking a Function and testing
"""


from random import randint


def attack_damage(modifier):
    roll = randint(1, 8)
    return modifier + roll


if __name__ == '__main__':
    result = attack_damage(10)
    print(result)
