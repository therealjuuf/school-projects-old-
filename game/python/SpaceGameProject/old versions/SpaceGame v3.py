import sys
import pygame
import time
import random

class  _Player(pygame.sprite.Sprite):
    def __init__(self,GameWorld, x, y):
        self.groups = GameWorld.AllSprites, GameWorld.PlayerSprite
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x=200
        self.y=300
        self.base_speed=5;
        self.bonus_speed=1
        self.main_sprite=pygame.image.load("Sprites/player/ship.png")
        self.sprite =pygame.transform.scale(self.main_sprite,(30,30))
        self.width=25+self.sprite.get_width()
        self.heigth=10+self.sprite.get_height()/2
        self.rect= (self.x,self.y,30,30)
        self.firespeed=0.1
        self.score=0
        self.fuel=100

    def render(self,window):
        window.blit(self.sprite, (self.x, self.y));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def move(self,pos):
        if (pos=="right"):
            self.x += self.base_speed*self.bonus_speed
        elif (pos == "left"):
            self.x -= self.base_speed*self.bonus_speed;
        elif(pos=="up"):
            self.y -=self.base_speed*self.bonus_speed;
        elif(pos=="down"):
            self.y +=self.base_speed*self.bonus_speed;
        if self.x>750: self.x=750
        if self.x<0: self.x=0
        if self.y>560: self.y=560
        if self.y<10: self.y=10
        self.rect= (self.x,self.y,30,30)

class SingleBullet(pygame.sprite.Sprite):
    def __init__(self,GameWorld,x,y,player_base_speed,bonus_vel):
        self.groups = GameWorld.AllSprites, GameWorld.BulletSprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x=x
        self.y=y
        self.velocity=bonus_vel+player_base_speed
        self.sprite = pygame.transform.scale(pygame.image.load("Sprites/player/SingleLaser.png"),(10,4))
        self.hitbox=(self.x,self.y,10,4);
        self.rect = pygame.Rect(self.x,self.y,10,4);
        self.GameWorld=GameWorld

    def move(self):
        self.x+=self.velocity
        self.rect=pygame.Rect(self.x,self.y,10,4)
        if(self.x>1000):
            self.kill()


    def render(self,window):
        window.blit(self.sprite, (self.x, self.y));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)






class _Enemy(pygame.sprite.Sprite):
    def __init__(self,GameWorld,x,y,velocity):
        self.groups = GameWorld.AllSprites, GameWorld.EnemySprites, GameWorld.EnemyUFOs
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = x
        self.y = y
        self.velocity = velocity
        self.sprite= pygame.transform.scale(pygame.image.load("Sprites/enemy/enemy1.png"),(30,30))
        self.rect = pygame.Rect(self.x,self.y,30,30)
        self.hitbox= (self.x,self.y,30,30)

    def move(self):
        self.x-=self.velocity
        self.rect = pygame.Rect(self.x, self.y, 30, 30)


    def render(self,window):
        window.blit(self.sprite, (self.x, self.y));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(window,(255,0,0),self.rect,2)


class _EnemyRocket(pygame.sprite.Sprite):
    def __init__(self,GameWorld,x,y,velocity,CreatedRock,Player):
        self.groups = GameWorld.AllSprites, GameWorld.EnemySprites, GameWorld.EnemyROCKETs
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x = x
        self.y = y
        self.velocity = velocity
        self.sprite= pygame.transform.scale(pygame.image.load("Sprites/enemy/rocket.png"),(30,30))
        self.rect = pygame.Rect(self.x,self.y,30,30)
        self.fired=0
        self.linkedRock=CreatedRock
        self.Target=Player

    def move(self):
        self.x-=self.linkedRock.velocity
        if(self.x-self.Target.x)<200 or self.fired ==1:
            self.fired=1
            self.y-=self.velocity
            self.rect = pygame.Rect(self.x, self.y, 30, 30)


class _Screen(object):
    def __init__(self):
        self.resolution=(800, 600)
        self.window=pygame.display.set_mode(self.resolution)
        self.bg=(pygame.transform.scale(pygame.image.load("Sprites/Bg/darkPurple.png"),self.resolution))
        self.bgWidth=self.bg.get_width()
        self.bgPosX1=0
        self.bgPosX2=self.bgWidth
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.mouse.set_visible(0)

    def getGameWindow(self):
        return pygame.display.set_mode(self.resolution)

    def renderBg(self):
        self.window.blit(self.bg,(self.bgPosX1,0));
        self.window.blit(self.bg,(self.bgPosX2,0))

    def BgMovement(self):
        self.bgPosX1 -= 1.4;
        self.bgPosX2 -= 1.4;
        if self.bgPosX1 < self.bgWidth * -1:
            self.bgPosX1 = self.bgWidth
        if self.bgPosX2 < self.bgWidth * -1:
            self.bgPosX2 = self.bgWidth


def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False









class _GameWorld:
    def __init__(self):
        self.AllSprites = pygame.sprite.Group()
        self.GroundSprites = pygame.sprite.Group()
        self.EnemySprites = pygame.sprite.Group()
        self.BulletSprites = pygame.sprite.Group()
        self.PlayerSprite=pygame.sprite.Group()
        self.EnemyUFOs = pygame.sprite.Group()
        self.EnemyROCKETs = pygame.sprite.Group()
        self.GameTime = time.time()
        self.Player_last_fire = time.time()
        self.Enemy_last_spawn = time.time()
        #self.Enemies = []
        #self.Bullets = []
        self.Player= _Player(self,300, 410);
        self.Screen=_Screen()
        self.Ground_last_spawn=time.time()
        self.LastSpawnX=2000

    def newWorld(self):
        pass

    def GenerateWorld(self,GroundAmount):
        for x in range(0,GroundAmount-1):
            SpawnY=random.randint(300,400)
            CreatedRock = Rock(self, x*500, SpawnY)
            if x>3:
                for a in range(0,random.randint(1,5)):
                    if(a==0): PosY=10
                    elif(a==1): PosY=5
                    elif(a==2):PosY=10
                    elif(a==3): PosY=5
                    elif(a==4):PosY=-8
                    self.EnemySprites.add(_EnemyRocket(self, CreatedRock.x+a*109, CreatedRock.y+110+PosY, 2.5, CreatedRock, self.Player))

    def EventListener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if keyPressed(pygame.K_LEFT): self.Player.move("left")
        if keyPressed(pygame.K_RIGHT): self.Player.move("right")
        if keyPressed(pygame.K_UP): self.Player.move("up")
        if keyPressed(pygame.K_DOWN): self.Player.move("down")
        if keyPressed(pygame.K_SPACE): self.CreateNewBullet()

    def CreateNewBullet(self):
        self.GameTime = time.time()
        if len(self.BulletSprites) < 25 and ((self.GameTime - self.Player_last_fire) > (0.3 - self.Player.firespeed)):
            self.Player_last_fire = time.time()
            self.BulletSprites.add(SingleBullet(self,(round(self.Player.x + self.Player.width // 2)), (round(self.Player.y + self.Player.heigth // 2)),self.Player.base_speed, 1))

    def CreateEnemy(self):
        if len(self.EnemyUFOs)<7:
            self.GameTime = time.time()
            if ((self.GameTime-self.Enemy_last_spawn)>1):
                self.Enemy_last_spawn = time.time()
                #self.Enemies.append(_Enemy(self,750,random.randint(20,500),2.5))
                self.EnemySprites.add(_Enemy(self, 805, random.randint(10, 400), 2.5))

    def RenderSprites(self):

        for sprite in self.GroundSprites:
            if sprite.x<200000 and sprite.x>-500:
                self.Screen.window.blit(sprite.sprite,(sprite.x, sprite.y))
                #pygame.draw.rect(self.Screen.window, (255, 0, 0), sprite.rect, 2)
            else:
                sprite.kill()

        for sprite in self.AllSprites:
            if sprite.x<200000 and sprite.x>-20:
                self.Screen.window.blit(sprite.sprite,(sprite.x, sprite.y))
                pygame.draw.rect(self.Screen.window, (255, 0, 0), sprite.rect, 2)
            else:
                sprite.kill()



class Rock(pygame.sprite.Sprite):
    def __init__(self,GameWorld, x, y, velocity=2):
        self.groups = GameWorld.GroundSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.rect= pygame.Rect(self.x,self.y,500,300)
        #self.sprite = pygame.transform.scale(pygame.image.load("Sprites/Ground/ground.png"),(300,300))
        self.sprite = pygame.transform.scale(pygame.image.load("Sprites/Ground/ground2.png"), (500, 300))
        self.velocity = velocity

    def move(self):
        # you don't need to check if running is true here, you're doing that in your loop
        self.x -= self.velocity
        #self.rect=pygame.Rect(self.x,self.y,2,400)

    def Render(self,GameWorld):
        #pygame.draw.rect(GameWorld.Screen.window, (255, 0, 0), self.rect, 0)
        #pygame.draw.rect(GameWorld.Screen.window, (255, 255, 255), self.rect, 3)
        pass


def main():


    #Player = _Player(300, 410);
    #screen = _Screen();

    GameWorld = _GameWorld()
    GameWorld.GenerateWorld(50)

    #_ship = GameWorld.Player.sprite

    y = random.randint(0, 400)

    while 1==1:

        GameWorld.Screen.renderBg();
        GameWorld.Screen.BgMovement();

        GameWorld.EventListener()

        pygame.sprite.groupcollide(GameWorld.BulletSprites,GameWorld.EnemySprites, True,True)
        #pygame.sprite.groupcollide(GameWorld.EnemySprites,GameWorld.GroundSprites,True,False)



        for bullet in GameWorld.BulletSprites:
            bullet.move()

        #GameWorld.GenerateGround()



        for rock in GameWorld.GroundSprites:
            rock.move()
            rock.Render(GameWorld)


        for enemy in GameWorld.EnemySprites:
            enemy.move()
                #enemy.render(GameWorld.Screen.window);

        GameWorld.RenderSprites()

        GameWorld.CreateEnemy()

        #GameWorld.Player.render(GameWorld.Screen.window);
        pygame.display.update()
        pygame.display.flip();

        GameWorld.Screen.clock.tick(60)



if __name__ == '__main__':
    main()



