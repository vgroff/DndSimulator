
def simulate1On1(character1, character2, vebrose = False):
    charArr = [character1, character2]
    if (character1.rollInitiative(vebrose) > character2.rollInitiative(vebrose)):
        currentIndex = 0
    else:
        currentIndex = 1
    
    while (character1.currentHitPoints != 0 and character2.currentHitPoints != 0):
        otherIndex = (currentIndex + 1) % 2
        charArr[currentIndex].attack(charArr[otherIndex], vebrose)
        currentIndex = (currentIndex + 1) % 2