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
#All EnemyTypes will have a MINIMUM roll of 5 and a MAXIMUM of 20

#First area Mobs
goblin = Monster("Goblin", 10, "Normal", 5, "Humanoid")

#Second area Mobs
zombie = Monster("Zombie", 5, "Normal", 5, "Undead")
solmyre = Monster("Zombie", 50, "Boss", 12, "Undead")
dreamrot = Monster("Zombie", 25, "MiniBoss", 8, "Undead")

#Third Area Mobs

#Fourth Area Mobs

#Fith Area Mobs

#Sixth area Boss and Mini Boss



#PlayerClass / PartyClass











# #Game Code
# def show_intro():
#     print(ascii_banner)
#     print("New Game Dev, Please Enjoy")
#     time.sleep(5)
#     getUsersName()
# def getUsersName():
# #Get Users Name
#     name = input("What is your name Stranger?: ")
#     print("Are you sure your name is " + name + "?")
#     isNameCorrect = False
# show_intro()