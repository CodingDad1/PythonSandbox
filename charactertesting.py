class Character():
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        print("Getting name")
        return self._name
    @name.setter
#
# Removed print statement to get rid of Setting name, because itll run automatically
# to actually set the name.
#
    def name(self, value):
        self._name = value
Nicco = Character("Nicco") # <----- This is calling the setter for name.
print(Nicco.name)
Nicco.name = "BigDickRandy"
print(Nicco.name)
Anything = Character("DickHead")
print(Anything.name)
print(Nicco.name)

player1 = Character("")


player1_name = input("Type in your name: ")
player1.name = player1_name
print("KILLED HIM " + player1.name + "!")


