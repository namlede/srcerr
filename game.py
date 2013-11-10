class Mob:
    def __init__(self):
        self.x=0
        self.y=0
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
    def __init__(self,newSpells):
        self.x=0
        self.y=0
        self.energy=1000
        self.health=10000
        self.states=[]
        self.spells=newSpells

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
        self.screen = pygame.display.set_mode((640,480))
        pygame.key.set_repeat(1, 1)
        pygame.display.set_caption('SrcError')
        self.playerSprite = Sprite(20, 400, 'player.png')
        self.player=Player()
        self.nouns=[self.player]
        self.spells=getSpells() #dictionary, name to class
    def cast(self,name):
        a=Spell(self)
        b=spells[name](a)
        a.setSpell(b)
        self.nouns.append(a)
    def getSpells(self):
        #initializes and gets all the spells, spells are passed the game
    def run(self):
        a=0
        for i in nouns:
            if(not i.run()):
                del nouns[a]
        a+=1
