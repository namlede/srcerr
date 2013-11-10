names=["Attack","Heal","SpiralAttack"]
class Attack: #shoots out a fieball that deals 4 damage to all mobs within radius of 100, dies after 100 ticks
        def __init__(self,newEffects):
                self.effects=newEffects
                self.ticks = 0
        def run(self):
                self.ticks += 1
                if self.ticks == 1:
                        self.effects.changeVelocity(10,10)
                self.effects.doDamageWithinRadius(40,100)
                if (self.ticks<=1000):
                        return True
                return False

class Heal: #heals the player if they are within a radius of 100, otherwise does nothing
#If the player is gone for 1000 consecutive ticks, then the spell will end permanently
        def __init__(self,newEffects):
                self.effects=newEffects
                self.end = 0
        def run(self):
                if (self.effects.getPlayerX()-self.effects.x)**2+(self.effects.getPlayerY()-self.effects.y)**2 <= 100:
                        self.end = 0
                        self.effects.healWithinRadius(50,100)
                else:
                        self.end += 1
                if (self.end<=50):
                        return True
                return False

class SpiralAttack: #spirals outward from the player, deals 10 damage to mobs if any are within a radius of 100
        def __init__(self,newEffects):
                self.effects=newEffects
                self.ticks = 0
                self.frame = 0
                self.m = 1
        def run(self):
        	self.ticks+=1
        	if self.ticks % 10 == 0:
			self.m += 10
			if self.ticks % 40 == 10:
				self.effects.changeVelocity(self.m,self.m)
			elif self.ticks % 40 == 20:
				self.effects.changeVelocity(self.m,-self.m)
			elif self.ticks % 40 == 30:
				self.effects.changeVelocity(-self.m,-self.m)
			elif self.ticks % 40 == 0:
				self.effects.changeVelocity(-self.m,self.m)
		creatures = self.effects.getNouns()
                for i in creatures:
                        if i.__class__.__name__=="Mob":
                                if (i.x-self.effects.x)**2+(i.y-self.effects.y)**2 <= 100:
                                        self.effects.doDamageWithinRadius(100,100)
                if (self.ticks<=50):
                        return True
                return False
