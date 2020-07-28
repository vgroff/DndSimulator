from utils import rollD20

class Character:
    def __init__(self, name, hitPoints, armourClass, weapon, initiative, nDamageDice = 1):
        self.name = name
        self.maxHitPoints = hitPoints
        self.currentHitPoints = self.maxHitPoints
        self.armourClass = armourClass
        self.weapon = weapon
        self.initiative = initiative
        self.nDamageDice = nDamageDice

    def rollInitiative(self, verbose = False):
        initiative = rollD20() + self.initiative
        if (verbose):
            print('{} rolled initiative {}'.format(self.name, initiative))
        return initiative

    def heal(self):
        self.currentHitPoints = self.maxHitPoints

    def attack(self, target, verbose = False):
        attackRoll = self.weapon.getAttackRoll()
        if (attackRoll > target.armourClass):
            damageRoll = self.weapon.getDamageRoll(self.nDamageDice)
            if verbose:
                print('{} attacked {} succesfully for {} damage'.format(self.name, target.name, damageRoll))
            target.takeDamage(damageRoll, verbose)
        elif verbose:
            print('{} failed to attack {}'.format(self.name, target.name))

    def takeDamage(self, damage, verbose = False):
        self.currentHitPoints = max(self.currentHitPoints - damage, 0)
        if verbose:
            print('{} took {} damage, now on {} hitpoints'.format(self.name, damage, self.currentHitPoints))