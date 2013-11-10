names=["Attack","Heal","SpiralAttack"]
class Attack: #shoots out a fiereball that deals 4 damage to all mobs within radius of 3, dies after 100 ticks
        def __init__(self,newEffects):
                self.effects=newEffects
                self.ticks = 0
        def run(self):
                self.ticks += 1
                if self.ticks == 1:
                        self.effects.changeVelocity(10,10)
                self.effects.doDamageWithinRadius(40,30)
                if (self.ticks<=1000):
                        return True
                return False

class Heal: #heals the player if they are within a radius of 2, otherwise does nothing
#If the player is gone for 1000 consecutive ticks, then the spell will end permanently
        def __init__(self,newEffects):
                self.effects=newEffects
                self.end = 0
        def run(self):
                creatures = self.effects.getNouns()
                for i in creatures:
                        if i.__class__.__name__=="Player":
                                if (i.x-self.effects.x)**2+(i.y-self.effects.y)**2 <= 2:
                                        self.end = 0
                                        self.effects.healWithinRadius(50,20)
                                else:
                                        self.end += 1
                if (self.end<=1000):
                        return True
                return False

class SpiralAttack: #spirals outward from the player, deals 10 damage to mobs if any are within a radius of 4
        def __init__(self,newEffects):
                self.effects=newEffects
                self.ticks = 0
        def run(self):
                self.ticks += 1
                if self.ticks % 4 == 1:
                        self.effects.changeVelocity(10,10)
                elif self.ticks % 4 == 2:
                        self.effects.changeVelocity(-10,10)
                elif self.ticks % 4 == 3:
                        self.effects.changeVelocity(-10,-10)
                elif self.ticks % 4 == 0:
                        self.effects.changeVelocity(10,-10)
                creatures = self.effects.getNouns()
                for i in creatures:
                        if i.__class__.__name__=="Mob":
                                if (i.x-self.effects.x)**2+(i.y-self.effects.y)**2 <= 4:
                                        self.effects.doDamageWithinRadius(100,40)
                if (self.ticks<=100):
                        return True
                return False
