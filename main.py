import utils
import Combat
from Weapon import MeleeWeapon
from Character import Character

import matplotlib.pyplot as plt

greataxe = MeleeWeapon(6, 12, 4)
talon2Handed = MeleeWeapon(7, 10, 5)
talon1Handed = MeleeWeapon(7, 8, 5)

options = [
    [Character('Ront', 37, 14, greataxe, 1), "Great Axe"],
    [Character('Ront', 37, 14, talon2Handed, 1), "Talon 2 Handed"],
    [Character('Ront', 37, 16, talon1Handed, 1), "Talon 1 Handed + Shield"],
    # [Character('Ront', 37, 14, MeleeWeapon(7, 10, 4), 1), "Talon 2 Handed (Only Damage Bonus)"],
    # [Character('Ront', 37, 14, MeleeWeapon(6, 10, 5), 1), "Talon 2 Handed (Only Hit Bonus)"]
]

morningStar = MeleeWeapon(4, 8, 2)
enemy = Character('Bugbear', 27, 16, morningStar, 2, nDamageDice = 2)

damageByRont = []
damageToRont = []
for (index, option) in enumerate(options):
    damageByRont.append(utils.Histogram(range(0, 18), True))
    damageToRont.append(utils.Histogram(range(0, 18), True))
    ront = option[0]
    for i in range(10000):
        ront.attack(enemy)
        enemy.attack(ront)
        damageByRont[index].add(enemy.maxHitPoints - enemy.currentHitPoints)
        damageToRont[index].add(ront.maxHitPoints - ront.currentHitPoints)
        ront.heal()
        enemy.heal()
        
ax1 = plt.subplot(1, 1, 1)
for (index, damageHist) in enumerate(damageByRont):
    ax1.plot(damageHist.buckets, damageHist.calcProportions(), label=options[index][1])
ax1.set_xlim(0, damageHist.buckets[-1] + 1)
ax1.set_ylim(0, 1)
ax1.set_yticks([0.1*i for i in range(11)])
ax1.set_ylabel("Cumulative Probability")
ax1.set_xlabel("Damage caused to Bugbear by Ront")
plt.legend()
plt.grid()
plt.show()

ax1 = plt.subplot(1, 1, 1)
for (index, damageHist) in enumerate(damageToRont):
    ax1.plot(damageHist.buckets, damageHist.calcProportions(), label=options[index][1])
ax1.set_xlim(0, damageHist.buckets[-1] + 1)
ax1.set_ylim(0, 1)
ax1.set_yticks([0.1*i for i in range(11)])
ax1.set_ylabel("Cumulative Probability")
ax1.set_xlabel("Damage caused to Ront by Bugbear")
plt.legend()
plt.grid()
plt.show()

ax1 = plt.subplot(1, 1, 1)
for option in options:
    ront = option[0]
    histogram = utils.Histogram(range(0, ront.maxHitPoints + 1), True)
    data = []
    for i in range(50000):
        Combat.simulate1On1(ront, enemy)
        histogram.add(ront.currentHitPoints)
        data.append(ront.currentHitPoints)
        ront.heal()
        enemy.heal()

    ax1.plot(histogram.buckets, histogram.calcProportions(), label=option[1])
ax1.set_xlim(0, ront.maxHitPoints)
ax1.set_ylim(0, 1)
ax1.set_ylabel("Cumulative Probability")
ax1.set_xlabel("Hitpoints Left By The End Of Combat Ront vs. Bugbear")
ax1.set_yticks([0.1*i for i in range(11)])
plt.legend()
plt.grid()
plt.show()