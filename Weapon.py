from utils import Advantage, rollD20, rollDn

class MeleeWeapon:
    def __init__(self, attackBonus, damageDice, damageBonus):
        self.attackBonus = attackBonus
        self.damageDice = damageDice
        self.damageBonus = damageBonus

    def getDamageRoll(self, dice = 1):
        damage = self.damageBonus
        for i in range(dice):
            damage += rollDn(self.damageDice)
        return damage

    def getAttackRoll(self, advantage = Advantage.none):
        return rollD20(advantage) + self.attackBonus