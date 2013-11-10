from pygame import *
import math
import spells
class Sprite:
    def __init__(self, xpos, ypos, filename):
	self.x = xpos
	self.y = ypos
	self.bitmap = image.load(filename)
	self.bitmap.set_colorkey((0,0,0))
    def set_position(self, xpos, ypos):
	self.x = xpos
	self.y = ypos
    def render(self):
        global screen
	screen.blit(self.bitmap, (self.x, self.y))
class Mob:
    def __init__(self,newGame):
        self.game = newGame
        self.radius = 100
        self.damage = 100
        self.x=20
        self.y=400
        self.health=10000
        self.states=[]
    def addState(self,a):
        states.append(a)
    def run(self):
        a=0
        for i in self.states:
            if(not i.run()):
                del self.states[a]
            a+=1
	if not (self.health>0):
		raise "You killed the mob!!!"
		print "WIN"
		print 4/0 
        if (self.game.player.x-self.x)**2+(self.game.player.y-self.y)**2<=self.radius**2:
                self.game.player.health -= self.damage
        
        return self.health>0
class Player:
    def __init__(self):
        self.x=20
        self.y=400
        self.energy=50000
        self.health=10000
        self.states=[]

    def run(self):
        self.energy+=100
        self.health+=0
	if self.health < 0 or self.energy < 0:
		raise "You died."
		print "DIE"
		print 4/0
		return False
class Spell:
    def __init__(self,newGame):
        self.game=newGame
        self.x=self.game.player.x
        self.y=self.game.player.y
        self.xvelocity=0
        self.yvelocity=0
    def setSpell(self,newUserSpell):
        self.userSpell=newUserSpell
    def run(self):
        self.x+=self.xvelocity
        self.y+=self.yvelocity
        self.alive = self.userSpell.run()
        return self.alive
    def getNouns(self):
        return self.game.nouns
    def doDamageWithinRadius(self,damage,radius):
        if (self.game.mob.x-self.x)**2+(self.game.mob.y-self.y)**2<=radius**2:
            self.game.mob.health-=damage
            self.game.player.energy-=radius+damage
    def healWithinRadius(self,heal,radius):
        if (self.game.player.x-self.x)**2+(self.game.player.y-self.y)**2<=radius**2:
            self.game.player.health+=heal
            self.game.player.energy-=radius+heal
    def changeVelocity(self,xChangeChange,yChangeChange):
        self.xvelocity+=xChangeChange
        self.yvelocity+=yChangeChange
        self.game.player.energy-=xChangeChange+yChangeChange
class Game:
    def __init__(self):
        init()
        global screen
        key.set_repeat(1, 1)
        display.set_caption('SrcError')
        self.playerSprite = Sprite(20, 400, 'player.png')
        self.mobSprite = Sprite(20, 400, 'mob.png')
        self.player=Player()
        self.mob=Mob(self)
        self.nouns=[self.player,self.mob]
        self.spellList=self.getSpells()
        self.activeSpells=[]
    def cast(self,index):
        a=Spell(self)
        b=self.spellList[index](a)
        a.setSpell(b)
        self.nouns.append(a)
        self.activeSpells.append([Sprite(self.playerSprite.x,self.playerSprite.y,'spell.png'),a])
    def getSpells(self):
        ret=[]
        for i in spells.names:
            ret.append(eval("spells."+i))
        return ret
    def run(self):
        global screen
        backdrop = image.load('backdrop.bmp')
        screen.blit(backdrop, (0, 0))
	for ourevent in event.get():
	    if ourevent.type == QUIT:
		quit = 1
	    if ourevent.type == KEYDOWN:
		if ourevent.key == K_RIGHT:
                    self.playerSprite.x += 20
                    self.player.x += 20
		if ourevent.key == K_LEFT:
		    self.playerSprite.x -=20
                    self.player.x -= 20
                if ourevent.key == K_DOWN:
		    self.playerSprite.y +=20
                    self.player.y += 20
                if ourevent.key == K_UP:
		    self.playerSprite.y -=20
                    self.player.y -= 20
		if ourevent.key == K_1:
		    self.cast(0)
		if ourevent.key == K_2:
		    self.cast(1)
		if ourevent.key == K_3:
		    self.cast(2)
        a=0
        for i in self.nouns:
            if(not i.run()):
                del self.nouns[a]
        self.player.run()
        if True:
            self.mobSprite.x-=int(0.02*(self.mob.x-self.player.x))
            self.mobSprite.y-=int(0.02*(self.mob.y-self.player.y))
            self.mob.x=self.mobSprite.x
            self.mob.y=self.mobSprite.y
        iterer=0
        for i in self.activeSpells:
            k=i[1].run()
            if(not k):
                del self.activeSpells[iterer]
                break
            i[0].x=i[1].x
            i[0].y=i[1].y
            i[0].render()
            iterer+=1
            
        a+=1
        self.mobSprite.render()
        self.playerSprite.render()
        print ["Energy: " + str(self.player.energy), "Health: " + str(self.player.health), "Mob Health: " + str(self.mob.health)]
        display.update()
	time.delay(5)
screen = display.set_mode((768,768))
a=Game()
for i in range(100000):
    a.run()
