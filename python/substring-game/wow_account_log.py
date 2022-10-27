#Characters per class
warrior = ["Zellane", "Wrathgore"]
mage = ["Fiz", "Gno", "Pyronear"]
paladin = ["Avenger", "Van"]
rogue = ["Ambusha", "Jackdaniels"]
hunter = ["Kroleez"]
death_knight = ["Evilsbane"]
shaman = ["Shielded"]

#Time played per class (summed)
def warrior_time_played(w1_played, w2_played):
    warrior_played = w1_played + w2_played
    print("Total warrior time played is: " + str(warrior_played), "hours.")
warrior_sum = warrior_time_played(1920, 960)
print(warrior_sum)
def mage_time_played(m1_played, m2_played, m3_played):
    mage_played = m1_played + m2_played + m3_played
    print("Total mage time played is: " + str(mage_played), "hours.")
mage_sum = mage_time_played(768, 700, 310)
print(mage_sum)
def paladin_time_played(p1_played, p2_played):
    paladin_played = p1_played + p2_played
    print("Total paladin time played is: " + str(paladin_played), "hours.")
paladin_sum = paladin_time_played(1200, 384)
print(paladin_sum)
def rogue_time_played(r1_played, r2_played):
    rogue_played = r1_played + r2_played
    print("Total rogue time played is: " + str(rogue_played), "hours.")
rogue_sum = rogue_time_played(888, 360)
print(rogue_sum)
hunter_sum = "Total hunter time played is: 1348 hours."
print(hunter_sum)
death_knight_sum = "Total death knight time played is: 400 hours."
print(death_knight_sum)
shaman_sum = "Total shaman time played is: 220 hours."
print(shaman_sum)

#Account time played
account_played = "Total account time played is: 9458 hours."
print(account_played)

#Item levels of character (practicing indexes and str's)
zellane_ilvl_txt = [warrior[0], "Item level:" +str(266)]
wrathgore_ilvl_txt = [warrior[1], "Item level:" +str(120)]
fiz_ilvl_txt = [mage[0], "Item level:" +str(202)]
gno_ilvl_txt = [mage[1], "Item level:" +str(135)]
pyronear_ilvl_txt = [mage[2], "Item level:" +str(40)]
avenger_ilvl_txt = [paladin[0], "Item level:" +str(160)]
van_ilvl_txt = [paladin[1], "Item level:" +str(205)]
ambusha_ilvl_txt = [rogue[0], "Item level:" +str(30)]
jackdaniels_ilvl_txt = [rogue[1], "Item level:" +str(145)]
kroleez_ilvl_txt = [hunter[0], "Item level:" +str(45)]
evilsbane_ilvl_txt = [death_knight[0], "Item level:" +str(55)]
shieled_ilvl_txt = [shaman[0], "Item level:" +str(25)]

#Character item levels (integer values only)
zellane_ilvl = 266
wrathgore_ilvl = 120
fiz_ilvl = 202
gno_ilvl = 135
pyronear_ilvl = 40
avenger_ilvl = 160
van_ilvl = 205
ambusha_ilvl = 30
jackdaniels_ilvl = 145
kroleez_ilvl = 45
evilsbane_ilvl = 55
shieled_ilvl = 25


#Item levels combined in 2d list
characters_ilvl = [
    zellane_ilvl, wrathgore_ilvl, fiz_ilvl, gno_ilvl, pyronear_ilvl, avenger_ilvl, van_ilvl, ambusha_ilvl, jackdaniels_ilvl, kroleez_ilvl, evilsbane_ilvl, shieled_ilvl
    ]
print(characters_ilvl)

#Determining highest item level character
def highest_ilvl_calc(characters_ilvl):
    highest_ilvl = max(characters_ilvl)
    if zellane_ilvl >= highest_ilvl:
        print("Zellane is your highest item level character! GO WARRIORS!!!")
    else:
        print("Zellane is not BiS.. sadge.")
highest_ilvl_calc(characters_ilvl)