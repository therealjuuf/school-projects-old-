import pygame


class SingleBullet(pygame.sprite.Sprite):
    def __init__(self,CurrentProcessor,x,y,player_base_speed,bonus_vel):
        self.groups = CurrentProcessor.Sprites.AllSprites, CurrentProcessor.Sprites.BulletSprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x=x
        self.y=y
        self.velocity=bonus_vel+player_base_speed
        self.sprite = pygame.transform.scale(pygame.image.load("Sprites/player/SingleLaser.png"),(10,4))
        self.hitbox=(self.x,self.y,10,4);
        self.rect = pygame.Rect(self.x,self.y,10,4);
        self.GameWorld=CurrentProcessor.GameWorld


    def move(self):
        self.x+=self.velocity
        self.rect=pygame.Rect(self.x,self.y,10,4)
        if(self.x>1000):
            self.kill()


    def render(self,window):
        window.blit(self.sprite, (self.x, self.y));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)



class SingleRocket(pygame.sprite.Sprite):
    def __init__(self,CurrentProcessor,x,y,player_base_speed,bonus_vel):
        self.groups = CurrentProcessor.Sprites.AllSprites, CurrentProcessor.Sprites.BulletSprites, CurrentProcessor.Sprites.RocketSprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x=x
        self.y=y
        self.velocity=bonus_vel+player_base_speed
        self.sprite = pygame.transform.scale(pygame.image.load("Sprites/player/SingleRocket.png"),(20,20))
        self.rotated=False
        self.rect = pygame.Rect(self.x,self.y,10,4);
        self.GameWorld=CurrentProcessor.GameWorld

    def move(self):

        if (self.velocity>-3):self.velocity-=2
        if(self.velocity<0):
            self.y-=self.velocity
            if(self.rotated==False):
                self.sprite=pygame.transform.rotate(self.sprite,-90)
                self.rotated=True
        else:
            self.y+=self.velocity
            self.x+=self.velocity+2

        self.rect=pygame.Rect(self.x,self.y,10,4)
        if(self.x>1000):
            self.kill()


    def render(self,window):
        window.blit(self.sprite, (self.x, self.y));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)


class _Enemy(pygame.sprite.Sprite):
    def __init__(self,CurrentProcessor,x,y,velocity):
        self.groups = CurrentProcessor.Sprites.AllSprites, CurrentProcessor.Sprites.EnemySprites, CurrentProcessor.Sprites.EnemySHIPs
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = x
        self.y = y
        self.velocity = velocity
        self.sprite= pygame.transform.scale(pygame.image.load("Sprites/enemy/enemy1.png"),(30,30))
        self.rect = pygame.Rect(self.x,self.y,30,30)
        #self.hitbox= (self.x,self.y,30,30)
        self.ScoreBonus=30

    def move(self):
        self.x-=self.velocity
        self.rect = pygame.Rect(self.x, self.y, 30, 30)


    def render(self,window):
        window.blit(self.sprite, (self.x, self.y));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(window,(255,0,0),self.rect,2)

class _EnemyUFO(pygame.sprite.Sprite):
    def __init__(self,CurrentProcessor,x,y,velocity):
        self.groups = CurrentProcessor.Sprites.AllSprites, CurrentProcessor.Sprites.EnemySprites, CurrentProcessor.Sprites.EnemyUFOs
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = x
        self.y = y
        self.starting_y=y
        self.direction="up"
        self.velocity = velocity
        self.sprite= pygame.transform.scale(pygame.image.load("Sprites/enemy/enemy2.png"),(30,30))
        self.rect = pygame.Rect(self.x,self.y,30,30)
        #self.hitbox= (self.x,self.y,30,30)
        self.ScoreBonus=40

    def move(self):
        if(self.y>=self.starting_y+30):
            self.direction="up"
        elif(self.y<self.starting_y-30):
            self.direction ="down"

        if(self.direction=="up"):self.y-=self.velocity
        elif(self.direction=="down"):self.y+=self.velocity

        self.x-=self.velocity
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        #self.sprite=pygame.transform.rotate(self.sprite,1)


    def render(self,window):
        window.blit(self.sprite, (self.x, self.y));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(window,(255,0,0),self.rect,2)


class _EnemyRocket(pygame.sprite.Sprite):
    def __init__(self,CurrentProcessor,x,y,velocity):
        self.groups = CurrentProcessor.Sprites.AllSprites, CurrentProcessor.Sprites.EnemySprites, CurrentProcessor.Sprites.EnemyROCKETs
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = x
        self.y = y
        self.velocity = velocity
        self.sprite= pygame.transform.scale(pygame.image.load("Sprites/enemy/rocket.png"),(30,30))
        self.rect = pygame.Rect(self.x,self.y,30,30)
        self.fired=0
        #self.linkedRock=CreatedRock
        self.Target=CurrentProcessor.Player
        self.ScoreBonus=25

    def move(self):
        self.x-=2
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        if(self.x-self.Target.x)<250 or self.fired ==1:
            self.fired=1
            self.y-=self.velocity


class _FuelBarrel(pygame.sprite.Sprite):
    def __init__(self,CurrentProcessor,x,y,velocity,CreatedRock):
        self.groups = CurrentProcessor.Sprites.AllSprites, CurrentProcessor.Sprites.ObjectSprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = x
        self.y = y
        self.velocity = velocity
        self.sprite= pygame.transform.scale(pygame.image.load("Sprites/Objects/barrel.png"),(30,30))
        self.rect = pygame.Rect(self.x,self.y,30,30)
        self.linkedRock=CreatedRock
        #self.Target=Player
        self.ScoreBonus=15
        self.FuelBonus=5

    def move(self):
        self.x -=self.linkedRock.velocity
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        #if(self.x-self.Target.x)<200 or self.fired ==1:
            #self.fired=1
            #self.y-=self.velocity




class Rock(pygame.sprite.Sprite):
    def __init__(self,CurrentProcessor, x, y, velocity=2):
        self.groups = CurrentProcessor.Sprites.GroundSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.rect= pygame.Rect(self.x,self.y,500,300)
        #self.sprite = pygame.transform.scale(pygame.image.load("Sprites/Ground/ground.png"),(300,300))
        self.sprite = pygame.transform.scale(pygame.image.load("Sprites/Ground/ground.png"), (500, 300))
        self.velocity = velocity

    def move(self):
        # you don't need to check if running is true here, you're doing that in your loop
        self.x -= self.velocity
        self.rect=pygame.Rect(self.x,self.y,500,300)

    def Render(self,GameWorld):
        #pygame.draw.rect(GameWorld.Screen.window, (255, 0, 0), self.rect, 0)
        #pygame.draw.rect(GameWorld.Screen.window, (255, 255, 255), self.rect, 3)
        pass

class Grass(pygame.sprite.Sprite):
    def __init__(self,CurrentProcessor, x, y, velocity=2):
        self.groups = CurrentProcessor.Sprites.GroundSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.rect= pygame.Rect(self.x,self.y,500,300)
        #self.sprite = pygame.transform.scale(pygame.image.load("Sprites/Ground/ground.png"),(300,300))
        self.sprite = pygame.transform.scale(pygame.image.load("Sprites/Ground/grass.png"), (500, 50))
        self.velocity = velocity

    def move(self):
        # you don't need to check if running is true here, you're doing that in your loop
        self.x -= self.velocity
        #self.rect=pygame.Rect(self.x,self.y,500,300)

    def Render(self,GameWorld):
        #pygame.draw.rect(GameWorld.Screen.window, (255, 0, 0), self.rect, 0)
        #pygame.draw.rect(GameWorld.Screen.window, (255, 255, 255), self.rect, 3)
        pass