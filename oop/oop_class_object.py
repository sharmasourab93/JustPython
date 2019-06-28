"""
Python: Object Oriented Programming
        Using Class Object
"""


class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing "+self.name+")")

        Robot.population += 1

    def die(self):
        """I am dying"""
        print(self.name + "is being destroyed!")

        Robot.population -= 1

        if Robot.population == 0:
            print(self.name+" was the last one")

        else:
            print("There are still {} robots walking".format(Robot.population))

    def say_hi(self):
        print("Greetings my masters call me "+ self.name)

    @classmethod
    def how_many(cls):
        print("we have {} robots".format(cls.population))


if __name__ == '__main__':
    droid1 = Robot("R2-D2")
    droid1.say_hi()
    Robot.how_many()

    droid2 = Robot("C-3P0")
    droid2.say_hi()
    Robot.how_many()

    print("Robots have finished their work. So let's destroy them.")
    droid2.die()
    droid1.die()
    print(Robot.die.__doc__)

    Robot.how_many()