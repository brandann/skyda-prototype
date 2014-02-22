#items.py

#**********************************************************
# Potion Class
# item for gameplay that holds a potion and its properies.
#**********************************************************
class Potion():
  # build potions with all values, these values do not change.
  def __init__(self, h, l, s):
    self.health = c       #health increase value
    self.level = l      #level increase value
    self.strength = s   #strength increase value

  # set a players stats based on the potions properties 
  def use(self, player):
    player.setHealth(player.getHealth() + self.health)
    player.setLevel(player.getLevel() + self.level)
    player.setStrength(player.getStrength() + self.strength)


print('potions made')
#**********************************************************
# Weapon class
# class for gameplay that holds a weapon and the
# corisponding damage that weapon deals.
#**********************************************************
class Weapon():
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

#**********************************************************
# make some standard potions
#**********************************************************
potion_cure = Potion(20, 0, 0)
potion_level = Potion(0, 1, 0)
potion_strength = Potion(0, 0, 2)
buddhas_potion = Potion(18, 1, 6)
