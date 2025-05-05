import random
#Character classes
class Character():
    def __init__(self, health, mana, armor, name, level, xp, currency, talent_points, dice_hit):
        self.health = health
        self.mana = mana
        self.armor = armor
        self.name = name
        self.level = level
        self.xp = xp
        self.currency = currency
        self.talent_points = talent_points
        self.dice_hit = dice_hit

    # The Dice Rolling Method
    def roll_dice(self, rolls, sides):
        return [random.randint(rolls, sides) for _ in range(rolls)]
        
    #health
    #This is a getter method (This is when you retive something)
    @property
    def health(self):
        return self._health
    #This is a setter method (When set the value of something)
    #health
    @health.setter
    def health(self, value):
        self._health = value
    #mana
    #This is a getter method (This is when you retive something)
    @property
    def mana(self):
        return self._mana
    #This is a setter method (When set the value of something)
    @mana.setter
    def mana(self, value):
        self._mana = value
    
    #armor
    #This is a getter method (This is when you retive something)
    @property
    def armor(self):
        return self._armor
    #This is a setter method (When set the value of something)
    @armor.setter
    def armor(self, value):
        self._armor = value
    
    #name
    #This is a getter method (This is when you retive something)
    @property
    def name(self):
        return self._name
    #This is a setter method (When set the value of something)
    @name.setter
    def name(self, value):
        self._name = value
    
    #level
    #This is a getter method (This is when you retive something)
    @property
    def level(self):
        return self._level
    #This is a setter method (When set the value of something)
    @level.setter
    def level(self, value):
        self._level = value

    #xp
    #This is a getter method (This is when you retive something)
    @property
    def xp(self):
        return self._xp
    #This is a setter method (When set the value of something)
    @xp.setter
    def xp(self, value):
        self._xp = value

    #currency
    #This is a getter method (This is when you retive something)
    @property
    def currency(self):
        return self._currency
    #This is a setter method (When set the value of something)
    @currency.setter
    def currency(self, value):
        self._currency = value

    #Talent_points
    #This is a getter method (This is when you retive something)
    @property
    def talent_points(self):
        return self._talent_points
    #This is a setter method (When set the value of something)
    @talent_points.setter
    def talent_points(self, value):
        self._talent_points = value

    #Dice_Hit
    #This is a getter method (This is when you retive something)
    @property
    def dice_hits(self):
        return self._dice_hits
    #This is a setter method (When set the value of something)
    @dice_hits.setter
    def dice_hits(self, value):
        self._dice_hits = value




Nicco = Character(150, 50, 10, "Nicco The Great", 1, 0, 0, 0, 0)
print(Nicco.health)
Brennan = Character (150, 50, 10, "Brennan the Goat", 1, 0, 0, 0, 0)
Nicco.dice_hits = Nicco.roll_dice(2, 20)
Brennan.dice_hits = Brennan.roll_dice(2, 20)
print(f"{Nicco.name} Rolled: {Nicco.dice_hits} (total: {sum(Nicco.dice_hits)})")
print(f"{Brennan.name} Rolled: {Brennan.dice_hits} (total: {sum(Brennan.dice_hits)})")