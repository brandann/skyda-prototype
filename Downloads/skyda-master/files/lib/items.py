#items.py

#**********************************************************
# Potion Class
# item for gameplay that holds a potion and its properies.
#**********************************************************
class Potion():
  cure = 0
  level = 0
  strength = 0
  def __init__(self, c, l, s):
    self.cure = c
    self.level = l
    self.strength = s

  # get the potions cure property
  def getCure(self):
    return self.cure

  # get the potions level gain property
  def getLevel(self):
    return self.level

  # get the potions strength gain property
  def getStrength(self):
    return self.strength

  # set the potions cure value
  def setCure(self, c):
    self.cure = c
    return

  # set the potions level gain value
  def setLevel(self, l):
    self.level = l
    return

  # set the potions strength gain value
  def setStrength(self, s):
    self.strength = s
    return


#### STANDARD POTIONS ####
potion_cure = Potion(20, 0, 0)
potion_level = Potion(0, 1, 0)
potion_strength = Potion(0, 0, 2)
buddhas_potion = Potion(18, 1, 6)

print('potions made')
#**********************************************************
# Weapon class
# class for gameplay that holds a weapon and the
# corisponding damage that weapon deals.
#**********************************************************
class Weapon():
  name = ''
  damage = 0
  def __init__(self, n, d):
    self.name = n
    self.damage = d

  #### SET METHODS ####
  def setName(self, name):
    self.name = name
  def setDamage(self, damage):
    self.damage = damage

  #### GET METHODS ####
  def getName(self):
    return self.name
  def getDamage(self):
    return self.damage

  #### DEPRECIATED ####
  def use(self):
    return self.getDamage()

#**********************************************************
# make some standard potions
#**********************************************************
