import time
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Mystvale")
#Monster Class
class Monster():
    def __init__(self, name, health, enemytype, armorlevel, family):
        self.name = name
        self.health = health
        self.enemytype = enemytype
        self.armorlevel = armorlevel
        self.family = family
#All Normal EnemyTypes will have a MINIMUM roll of 5
goblin = Monster("Goblin", 10, "Normal", 5, "Humanoid")
zombie = Monster("Zombie", 5, "Normal", 5, "Undead")

def show_intro():
    print(ascii_banner)
    print("New Game Dev, Please Enjoy")
    time.sleep(5)
    getUsersName()
def getUsersName():
#Get Users Name
    name = input("What is your name Stranger?: ")
    print("Are you sure your name is " + name + "?")
    isNameCorrect = False
show_intro()