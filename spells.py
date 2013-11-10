names=["Attack"]
class Fireball:
	def __init__(self,newEffects):
		self.effects=newEffects
		self.ticks = 0
	def run(self):
		self.ticks += 1
		if self.ticks = 1:
			self.effects.changeVelocity(10,10)
		self.effects.doDamageWithinRadius(4,3)
		return self.ticks <=100
