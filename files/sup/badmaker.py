#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brandan
#
# Created:     12/02/2014
# Copyright:   (c) brandan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randint

a = []

in_file = open( "names.txt", "r")
for line in in_file:
    a.append( line.strip() )
in_file.close()

a.sort()

out_file = open("bad.txt", "w")
for name in a:
    if len(name) < 8:
        r1 = randint(1,10)
        r2 = randint(1,20)
        out_file.write("# " + name + '\n')
        out_file.write("player_" + name.lower() + " = Player()" + '\n')
        out_file.write('player_' + name.lower() + '.setName("' + name + '")' + '\n')
        out_file.write("player_" + name.lower() + ".setLevel(" + str(r1) + ")" + '\n')
        out_file.write("player_" + name.lower() + ".setGold(" + str(r1 * r2) + ")" + '\n')
        out_file.write('baddies.append(player_' + name.lower() + ')\n')
        out_file.write('\n')
out_file.close()

print('done')