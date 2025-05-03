import time
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Mystvale")

def show_intro():
    print(ascii_banner)
    print("New Game Dev, Please Enjoy")
    time.sleep(5)
    getUsersName()
def getUsersName():
#Get Users Name
    name = input("What is your name warrior: ")
    print("Are you sure your name is " + name + "?")
    isNameCorrect = False
show_intro()
