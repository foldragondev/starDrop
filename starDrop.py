#This concept is from the mobile game Brawl Stars by Supercell
#This concept demonstrates how the star drop can attract players
#Also this code is made by a student so it might not be the cleanest

#The random library is for the randomness of the star drop
#So the player might get something very rare
import random
import time
from collections import Counter

#Tiering system makes the player get very happy when they get high tier rewards
tier = ["Rare", "Super Rare", "Epic", "Mythic", "Legendary"]

#The main star drop mechanics
def starDrop():
    #The numbers represent the tier(from the tier list)
    rarity = 0
    print(tier[rarity])
    for i in range(4):
        #You get the player to tap the screen
        #a = input()
        #But for demonstration purposes I use time.sleep
        time.sleep(.05)
        #Then there's a chance for rarity upgrade, thge higher current rarity, the harder upgrade
        if random.randint(1, (rarity+1)*3) == 1: #Some simple calculations for chance of upgrade
            rarity += 1
        #Print out the rarity, normally they use huge text to make it look dramatic
        print(tier[rarity])
    return rarity

#Test use
results = []
for i in range(20):
    results.append(starDrop())
    print("\n\n")
#Print out all results
results.sort()
counts = Counter(results)
for item in sorted(counts.keys()):
    print(f"{tier[item]} x {counts[item]}")