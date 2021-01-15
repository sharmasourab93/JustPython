"""
Python: Switch Case

switch is a statement that evaluates the accuracy or
similarity of the value of a certain input.

Reference: https://matteoguadrini.github.io/posts/a-switch-story/
"""


# Switch working in Bash
"""
echo -n "Enter the name of a fruit"
read FRUIT

echo -n "The $FRUIT is"

case $FRUIT in

    apple)
        echo -n "apple"
        ;;
    banana)
        echo -n "banana"
        ;;
    blueberries | raspberries | "blue currant" | currant)
        echo -n "berries"
        ;;
    *)
        echo -n "Unknown"
        ;;
esac
"""

# An equivalent code in python would look like
#Python does not have any switch statements.
# A PEP 3103 has been evaluated and created, but the conclusion is:

# Python is fine without a switch statement,
# and perhaps those who claim it would be a mistake
# to add one are right.
"""
fruit = "banana"
if fruit == "apple":
    print("The fruit is apple")
elif fruit == "banana":
    print("The fruit is banana")
elif fruit in ("blueberries","raspberries", "blue currant", "currant"):
    print("The fruit is berries")
else:
    print("The fruit is unknown")
"""

# A simple hash indexes, it is much faster in retrieving values.
"""
my_fruit = "banana"
fruits = {
    "apple": "This fruit is apple",
    "banana": "The fruit is banana",
    "blueberries": "The fruit is berries",
    "raspberries": "The fruit is berries",
    "blue currant": "The fruit is berries",
    "currant": "The fruit is berries"
}
print(fruits.get(my_fruit, "The fruit is unknown"))
"""


# A callable switch
def switch(match, dictionary, default="no match"):
    for key in dictionary.keys():
        if match in key:
            switch.last_match = key
            return dictionary.get(key)
        
    return default


calc = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y
    }


plus = switch('plus', calc, default="unintended function")
minus = switch('minus', calc, default="unintended function")


print("Plus: {0}".format(plus(6, 4)))
print("Minus: {0}".format(minus(6, 4)))
