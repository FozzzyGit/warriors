from random import randint
class Warrior:
    health = 100
    damage = 20
    def getHealth(self):
        return self.health


first = Warrior()
second = Warrior()
while first.health*second.health != 0:
    if randint(1,2) == 1:
        second.health -=20
        print("First warrior hits second, and second's HP now =", second.getHealth())

    else:
        first.health -=20
        print("Second warrior hits first, and first's HP now =", first.getHealth())
if first.health > 0:
    print("FIRST WARRIOR WIN")
else:
    print("SECOND WARRIOR WIN")