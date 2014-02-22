from items import Potion, buddhas_potion
#**********************************************************
# Player (player.py)
# Player class is the main character class. can also be
# adapted for bad guys, or non playable helping
# characters!
#**********************************************************
class Player():

  def __init__(self):
    self.name = 'Renaldo Moon'
    self.level = 1
    self.health = 10
    self.experience = 0
    self.alive = True
    self.invetory = []
    self.potion = None
    self.potion_bool = False
    self.gold = 0
    self.strength = 3

  ############ GET METHODS ############

  #return the players name
  def getName(self):
    return self.name

  #return level of player
  def getLevel(self):
    return self.level

  #return health of player
  def getHealth(self):
    return self.health

  #return experience of player
  def getExperience(self):
    return self.experience

  #return invetory list of player
  def getInvetory(self):
    return self.invetory

  #return potion object of player
  def getPotion(self):
    return self.potion

  #return gold of player
  def getGold(self):
    return self.gold

  #return strength of player
  def getStrength(self):
    return self.strength

  #return players dealing damage
  def getAttack(self):
    return_damage = self.level * self.strength
    self.gainExp(return_damage)
    return return_damage

  #return if player has potion object
  def hasPotion(self):
    return self.potion_bool


  ############ SET METHODS ############

  #set the players name
  def setName(self, n):
    self.name = n

  #sets players level
  def setLevel(self, l):
    self.level = l
    self.setHealth(l*10)

  #sets players health
  def setHealth(self, h):
    self.health = h

  #sets players experience
  def setExperience(self, e):
    self.experience = e

  #add an item to the players invetory
  def addItem(self, item):
    self.invetory.append(item)
    self.invetory.sort()

  #sets players potion to p
  def setPotion(self, p):
    self.potion = p
    self.potion_bool = True

  #sets players gold
  def setGold(self, g):
    self.gold = g

  #set players strength
  def setStrength(self, s):
    self.strength = s

  ############ ACTION METHODS ############

  #gain experience points, and manage level
  #advancing from experience gain
  def gainExp(self, n):
    self.experience += n
    if self.experience >= self.level * 20:
      overage = self.experience - self.level * 20
      self.level += 1
      self.experience = overage

  #recives an attack from anouther player
  def reciveAttack(self, hit):
    self.health -= hit
    if self.health < 1:
      self.health = 0
      self.die()

  #use potion for health, set potion to None
  def usePotion(self):
    self.potion.use(self)
    if self.health > (self.level * 10):
      self.health = self.level * 10
    self.potion_bool = False

  def die(self):
    self.alive = False

#**********************************************************
# showPlayerStats
# prints out a chart of all the players stats. used for
# testing and tracing through the player object.
#**********************************************************
def showPlayerStats(player):
    print('\n******************************************')
    print(player.name + ' stats')
    print('level: ' + str(player.getLevel()))
    print('health: ' + str(player.getHealth()))
    print('experience: ' + str(player.getExperience()))
    print('alive: ' + str(player.alive))
    print('invetory: ' + str(player.getInvetory()))
    print('potion: ' + str(player.getPotion()))
    print('gold: ' + str(player.getGold()))
    print('strength: ' + str(player.getStrength()))
    print('******************************************\n')

#**********************************************************
# MAIN PLAYER FUNCTION (FOR TESTING)
#**********************************************************
def main():

  #### set up some standard bad guys ####
  mouse = Player()
  mouse.name = 'Mouse Man'
  mouse.setLevel(2)

  mouse.setPotion(buddhas_potion)

  fish = Player()
  fish.name = 'Fish Buddy'
  fish.setLevel(1)

  showPlayerStats(mouse)
  mouse.usePotion()
  showPlayerStats(mouse)

  fish.reciveAttack(mouse.getAttack())
  showPlayerStats(fish)

  #showPlayerStats(mouse)
  #mouse.reciveAttack(103)
  #showPlayerStats(mouse)

if __name__ == '__main__':
    main()
