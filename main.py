#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      player_main
#
# Created:     12/02/2014
# Copyright:   (c) player_main 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import standard library items
from random import randint
import os, sys, time, platform

#import my library items
lib_path = os.path.abspath('files/lib')
sys.path.append(lib_path)
from player import Player
from player_profile import baddies
from items import *

#import my suport items
sup_path = os.path.abspath('files/sup')
sys.path.append(sup_path)
from Blogo10 import logo10

#reset path to root
base_path = os.path.abspath('../..')
sys.path.append(base_path)

#make clear screen work on either system
if platform.system() == 'Windows':
    clean = 'cls'   #Windows
    os.system('color 0e')
else:
    clean = 'clear' #Linux/Unix

# Main game loop
def main():
    
    pause = 1
    # show logo information
    os.system(clean)
    logo10()
    time.sleep(pause)
    os.system(clean)

    print('''
     .-'
'--./ /     _.---.
'-,  (__..-`       \\
   \\          .     |
    `,.__.   ,__.--/
      '._/_.'___.-`

''')
    a = raw_input('A wizard has turned you into a whale!\nWhat is your name?\n\n')
    # set up player_main
    player_main = Player()
    player_main.setName(a)
    player_main.setLevel(5)
    
    os.system(clean)
    print('Well ' + player_main.getName() + ', that is trully bad furtune.')
    time.sleep(pause*2)
    print('come with me and I will return you back to your original form.')
    time.sleep(pause*2)

    # give player_main a potion to start with
    print('Here, take this potion, this land is dangerous.')
    player_main.setPotion(buddhas_potion)
    time.sleep(pause)
    
    print(player_main.getName().upper() + '! LOOK OUT!')
    time.sleep(pause*2)

    # pick random enemy
    player_enemy = baddies[randint(0,len(baddies)-1)]
    
    # print title
    os.system(clean)
    print(player_main.getName() + ' vs ' + player_enemy.getName())
    time.sleep(pause)
    
    # track turns
    turn = True

    # main game loop
    while player_main.alive and player_enemy.alive:

        # turn == True is player_main turn
        if turn:
            # give options for gameplay
            display(player_main, player_enemy)
            print("1: fight")
            print("2: potion")
            a = raw_input('\nEnter action...')
            
            # act on option
            if a == '2':
                if player_main.hasPotion():
                    #use potion
                    display(player_main, player_enemy)
                    print(player_main.getName() + ' uses a potion')
                    time.sleep(pause)
                    player_main.usePotion()
                    # switch turns
                    turn = False
                else:
                    display(player_main, player_enemy)
                    raw_input('you do not have any potions...')
            else:
                # attack player_enemy
                display(player_main, player_enemy)
                print( player_main.getName() + " Attacks...")
                time.sleep(pause)
                player_enemy.reciveAttack(player_main.getAttack())
                print(str(player_main.getAttack()) + ' Damage done to ' + player_enemy.getName())
                time.sleep(pause)
                # switch turns
                turn = False
        else:
            display(player_main, player_enemy)
            print(player_enemy.getName() + "'s turn")
            time.sleep(pause)
            # enemy attacks
            display(player_main, player_enemy)
            print(player_enemy.getName() + " Attacks!")
            time.sleep(pause)
            display(player_main, player_enemy)
            print(str(player_enemy.getAttack()) + ' Damage done to ' + player_main.getName())
            time.sleep(pause)
            player_main.reciveAttack(player_enemy.getAttack())
            
            # switch turns
            turn = True
    
    # display winnings
    if player_main.alive:
      #player_main wins
      display(player_main, player_enemy)
      print(player_main.getName() + ' WINS')
      time.sleep(pause)
      
      # find gold
      dropped = player_enemy.getGold()
      display(player_main, player_enemy)
      print(player_enemy.getName() + ' dropped ' + str(player_enemy.getGold()) + ' gold!')
      time.sleep(pause)

      os.system(clean)
      print('Wow, that was close!')
      print('I think you will do just fine in this magical land...')
      a = raw_input('')
      
    else:
      #player_enemy wins
      display(player_main, player_enemy)
      print(player_main.getName() + ' LOST')
      time.sleep(pause)
      print(player_main.getName() + ' dropped ' + str(player_main.getGold()) + ' gold!')
      time.sleep(pause)

def display(p1, p2):
    os.system(clean)
    print('_______________________________')
    print('  ' + p1.getName() + ', lvl ' + str(p1.getLevel()))
    print('  HP: ' + str(p1.getHealth()))
    print('\n  ' + p2.getName() + ', lvl ' + str(p2.getLevel()))
    print('  HP: ' + str(p2.getHealth()))
    print('_______________________________\n')
    
def entryMessage():
  print('not implemented')
    
if __name__ == '__main__':
    main()
