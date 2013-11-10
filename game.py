from pygame import *
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
    def __init__(self):
        self.x=20
        self.y=400
        self.health=10000
        self.states=[]
    def addState(self,a):
        states.append(a)
    def run(self):
        a=0
        for i in self.states:
            if(!i.run()):
                del self.states[a]
            a+=1
        
        return self.health>0
class Player:
    def __init__(self):
        self.x=20
        self.y=400
        self.energy=1000
        self.health=10000
        self.states=[]

    def run(self):
        self.energy+=10
        self.health+=10
        a=0
        for i in self.states:
            if(!i.run()):
                del self.states[a]
            a+=1
        return self.health>0
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
        self.x+=self.xveloctiy
        self.y+=self.yveloctiy
        self.userSpell.run()
    def getNouns(self):
        return self.game.nouns
    def doDamgeWithinRadius(self,damage,radius):
        for i in self.game.nouns:
            if i.__class__.__name__=="Mob":
                if (i.x-self.x)**2+(i.y-self.y)**2<=radius**2:
                    i.health-=damage
                    self.game.player.energy-=radius+damage
     def healWithinRadius(self,heal,radius):
        for i in self.game.nouns:
            if i.__class__.__name__=="Player":
                if (i.x-self.x)**2+(i.y-self.y)**2<=radius**2:
                    i.health+=heal
                    self.game.player.energy-=radius+heal
    def changeVelocity(self,xChangeChange,yChangeChange):
        self.xChange+=xChangeChange
        self.yChange+=yChangeChange
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
        self.mob=Mob()
        self.nouns=[self.player,self.mob]
        self.spells=getSpells()
        self.activeSpells=[]
    def cast(self,index):
        a=Spell(self)
        b=spells[index](a)
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
        screen.blit(backdrop, (0, 0))
	for ourevent in event.get():
	    if ourevent.type == pygameQUIT:
		quit = 1
	    if ourevent.type == KEYDOWN:
		if ourevent.key == K_RIGHT:
                    self.playerSprite.x += 20
                    self.player.x += 20
		if ourevent.key == K_LEFT:
		    self.playerSprite.x -=20
                    self.player.x -= 20
                if ourevent.key == K_DOWN:
		    self.playerSprite.y -=20
                    self.player.y -= 20
                if ourevent.key == K_UP:
		    self.playerSprite.y +=20
                    self.player.y += 20
		if ourevent.key == K_1:
		    self.cast(1)
		if ourevent.key == K_2:
		    self.cast(2)
		if ourevent.key == K_3:
		    self.cast(3)
        a=0
        for i in nouns:
            if(not i.run()):
                del nouns[a]
        scale=100/((self.mob.x-self.player.x)**2+(self.mob.y-self.player.y)**2)
        self.mobSprite.x=scale*(self.mob.x-self.player.x)+20
        self.mobSprite.y=scale*(self.mob.y-self.player.y)+400
        self.mob.x=self.mobSprite.x
        self.mob.y=self.mobSprite.y
        for i in self.activeSpells:
            i[0].x=i[1].x
            i[0].y=i[1].y
            i[0].render()
        a+=1
        self.mobSprite.render()
        self.playerSprite.render()
        
        display.update()
	time.delay(5)
screen = display.set_mode((640,480))
