#-------------------------------------------------------------------------------
# Name:        brandanvscorey
# Purpose:     a testing game main that uses the standard player and items
#              classes to battle between brandan and corey
#
# Author:      brandan
#
# Created:     02/11/2014
#-------------------------------------------------------------------------------

from player import Player, showPlayerStats
from items import *
import os

def main():

    print('FIGHT!!!!\n')

    #build player objects
    brandan = Player()
    corey = Player()

    #set up brandan
    brandan.setName('Brandan')
    brandan.setPotion(buddhas_potion)

    #set up corey
    corey.setName('Corey')
    corey.setPotion(potion_cure)

    print('initial stats')
    showPlayerStats(brandan)
    showPlayerStats(corey)

    a = raw_input('press enter')
    os.system('cls')

    #corey hits brandan
    print('\nCorey hits Brandan\n')
    print('brandans health: ' + str(brandan.getHealth()))
    brandan.reciveAttack(corey.getAttack())
    print('brandans health after getting hit: ' + str(brandan.getHealth()))

    showPlayerStats(brandan)
    showPlayerStats(corey)

    a = raw_input('press enter')
    os.system('cls')

    #get some gold
    print('brandan finds 23 gold!')
    brandan.gold += 23
    showPlayerStats(brandan)

    a = raw_input('press enter')
    os.system('cls')

    #use potions
    print('brandan uses a potion')
    brandan.usePotion()
    showPlayerStats(brandan)

    a = raw_input('press enter')
    os.system('cls')

    #brandan hit corey
    print('\nBrandan hits Corey\n')
    corey.reciveAttack(brandan.getAttack())
    showPlayerStats(brandan)
    showPlayerStats(corey)

    a = raw_input('press enter')
    os.system('cls')

if __name__ == '__main__':
    main()
