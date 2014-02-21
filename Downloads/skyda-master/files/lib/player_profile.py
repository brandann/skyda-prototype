###########################################################
## player profile
## standard profiles for multiuse disposable characters
###########################################################
from player import Player

###### BAD GUYS ######
baddies = []

# Adda
player_adda = Player()
player_adda.setName("Adda")
player_adda.setLevel(2)
player_adda.setGold(14)
baddies.append(player_adda)

# Aela
player_aela = Player()
player_aela.setName("Aela")
player_aela.setLevel(4)
player_aela.setGold(80)
baddies.append(player_aela)

# Aeris
player_aeris = Player()
player_aeris.setName("Aeris")
player_aeris.setLevel(6)
player_aeris.setGold(114)
baddies.append(player_aeris)

# Aveline
player_aveline = Player()
player_aveline.setName("Aveline")
player_aveline.setLevel(8)
player_aveline.setGold(160)
baddies.append(player_aveline)

# Bastila
player_bastila = Player()
player_bastila.setName("Bastila")
player_bastila.setLevel(2)
player_bastila.setGold(28)
baddies.append(player_bastila)

# Clover
player_clover = Player()
player_clover.setName("Clover")
player_clover.setLevel(5)
player_clover.setGold(75)
baddies.append(player_clover)

# Cortana
player_cortana = Player()
player_cortana.setName("Cortana")
player_cortana.setLevel(9)
player_cortana.setGold(126)
baddies.append(player_cortana)

# Flemeth
player_flemeth = Player()
player_flemeth.setName("Flemeth")
player_flemeth.setLevel(4)
player_flemeth.setGold(20)
baddies.append(player_flemeth)

# Juhani
player_juhani = Player()
player_juhani.setName("Juhani")
player_juhani.setLevel(7)
player_juhani.setGold(14)
baddies.append(player_juhani)

# Kitana
player_kitana = Player()
player_kitana.setName("Kitana")
player_kitana.setLevel(7)
player_kitana.setGold(56)
baddies.append(player_kitana)

# Leliana
player_leliana = Player()
player_leliana.setName("Leliana")
player_leliana.setLevel(7)
player_leliana.setGold(35)
baddies.append(player_leliana)

# Liara
player_liara = Player()
player_liara.setName("Liara")
player_liara.setLevel(4)
player_liara.setGold(52)
baddies.append(player_liara)

# Morenn
player_morenn = Player()
player_morenn.setName("Morenn")
player_morenn.setLevel(4)
player_morenn.setGold(76)
baddies.append(player_morenn)

# Nova
player_nova = Player()
player_nova.setName("Nova")
player_nova.setLevel(6)
player_nova.setGold(54)
baddies.append(player_nova)

# Silver
player_silver = Player()
player_silver.setName("Silver")
player_silver.setLevel(8)
player_silver.setGold(32)
baddies.append(player_silver)

# Tallis
player_tallis = Player()
player_tallis.setName("Tallis")
player_tallis.setLevel(7)
player_tallis.setGold(91)
baddies.append(player_tallis)

# Ysolda
player_ysolda = Player()
player_ysolda.setName("Ysolda")
player_ysolda.setLevel(9)
player_ysolda.setGold(99)
baddies.append(player_ysolda)

def main():
    print('Name\t\tLevel\tGold')
    for b in baddies:
        print(b.getName() + '\t\t' + str(b.getLevel()) + '\t\t' + str(b.getGold()))

if __name__ == '__main__':
    main()