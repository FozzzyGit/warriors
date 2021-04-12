from random import randint
class Warrior:
    health = 100
    def hit_myself(self):
        self.health-=20
    def getHealth(self):
        return self.health


first = Warrior()
second = Warrior()
while first.health*second.health != 0:
    if randint(1,2) == 1:
        first.hit_myself()
        print("Second warrior hits first, and first's HP now =", first.getHealth())
    else:
        second.hit_myself()
        print("First warrior hits second, and second's HP now =", second.getHealth())
if first.health > 0:
    print("FIRST WARRIOR WIN")
else:
    print("SECOND WARRIOR WIN")