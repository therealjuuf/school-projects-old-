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
        self.rect= pygame.Rect(self.x,self.y,30,30)
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
        self.rect= pygame.Rect(self.x,self.y,30,30)

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
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        if(self.x-self.Target.x)<200 or self.fired ==1:
            self.fired=1
            self.y-=self.velocity



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
    def __init__(self,Screen,Processor):
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
        self.Screen=Screen
        self.Active=False
        self.Initialized=False
        self.CurrentProcessor=Processor
        self.LastGameStop=time.time()


    def newWorld(self):
        pass

    def GenerateWorld(self,GroundAmount):
        for x in range(0,GroundAmount-1):
            SpawnY=random.randint(400,600)
            CreatedRock = Rock(self, x*500, SpawnY)
            GrassYSub=(random.randint(30,50))
            self.GroundSprites.add(Grass(self, x*500, SpawnY-GrassYSub))
            if x>3:
                for a in range(0,random.randint(1,5)):
                    if(a==0): PosY=6
                    elif(a==1): PosY=2
                    elif(a==2):PosY=7
                    elif(a==3): PosY=2
                    elif(a==4):PosY=-4
                    self.EnemySprites.add(_EnemyRocket(self, CreatedRock.x+a*109, CreatedRock.y-5+PosY-GrassYSub, 2.5, CreatedRock, self.Player))

    def EventListener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        if keyPressed(pygame.K_ESCAPE):
            if (self.Active == True and self.GameRealTime-self.LastGameStop>0.2):
                self.LastGameStop=time.time()
                self.Active = False
            elif(self.Active == False and self.GameRealTime-self.LastGameStop>0.2):
                self.LastGameStop=time.time()
                self.Active = True

        #Player Events while game is active
        if(self.Active==True):
            if keyPressed(pygame.K_LEFT): self.Player.move("left")
            if keyPressed(pygame.K_RIGHT): self.Player.move("right")
            if keyPressed(pygame.K_UP): self.Player.move("up")
            if keyPressed(pygame.K_DOWN): self.Player.move("down")
            if keyPressed(pygame.K_SPACE): self.CreateNewBullet()
            if keyPressed(pygame.K_r):
                self.PlayerDeath()







    def CreateNewBullet(self):
        self.GameTime = time.time()
        if len(self.BulletSprites) < 25 and ((self.GameTime - self.Player_last_fire) > (0.3 - self.Player.firespeed)):
            self.Player_last_fire = time.time()
            self.BulletSprites.add(SingleBullet(self,(round(self.Player.x + self.Player.width // 2)), (round(self.Player.y + self.Player.heigth // 2)),self.Player.base_speed, 1))

    def CreateEnemy(self):
        if len(self.EnemyUFOs)<7:

            if ((self.GameTime-self.Enemy_last_spawn)>1):
                self.Enemy_last_spawn = time.time()
                #self.Enemies.append(_Enemy(self,750,random.randint(20,500),2.5))
                self.EnemySprites.add(_Enemy(self, 805, random.randint(10, 400), 3))

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

    def PlayerDeath(self):
        self.Active = False
        EndScreen = _EndScreen(self.Screen)
        EndScreen.Processor(self, self.CurrentProcessor)
    def EnemyDeath(self):
        self.Player.score +=50

    def Initialize(self):
        self.Screen.window.fill((0, 0, 0))
        TextOnScreen(self.Screen, "Initializing...", 30, 50, 200)
        self.GenerateWorld(50)
        self.Initialized=True

    def Processor(self):
        self.EventListener()
        self.GameRealTime = time.time()
        if (self.Active == True):
            if(self.Initialized==False): self.Initialize()

            self.Screen.renderBg();
            self.Screen.BgMovement();

            self.GameTime = time.time()

            if(pygame.sprite.groupcollide(self.BulletSprites, self.EnemySprites, True, True)): self.EnemyDeath()
            if pygame.sprite.groupcollide(self.PlayerSprite,self.EnemySprites,False,False): self.PlayerDeath()
            if pygame.sprite.groupcollide(self.PlayerSprite,self.GroundSprites,False,False): self.PlayerDeath()
            # pygame.sprite.groupcollide(GameWorld.EnemySprites,GameWorld.GroundSprites,True,False)

            for bullet in self.BulletSprites:
                bullet.move()

            # GameWorld.GenerateGround()

            for rock in self.GroundSprites:
                rock.move()
                #rock.Render(self)


            for enemy in self.EnemySprites:
                enemy.move()
                # enemy.render(GameWorld.Screen.window);

            self.RenderSprites()

            self.CreateEnemy()

            TextOnScreen(self.Screen, "Your Score: "+str(self.Player.score), 30, 500, 550)

            pygame.display.update()
            pygame.display.flip();

            self.Screen.clock.tick(60)
            # GameWorld.Player.render(GameWorld.Screen.window);

        elif(self.CurrentProcessor.StartScreen.Active==False):
            TextOnScreen(self.Screen, "Game Stopped!", 30,
                         50, 550)
            pygame.display.flip();

            self.Screen.clock.tick(60)






class Rock(pygame.sprite.Sprite):
    def __init__(self,GameWorld, x, y, velocity=2):
        self.groups = GameWorld.GroundSprites
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
    def __init__(self,GameWorld, x, y, velocity=2):
        self.groups = GameWorld.GroundSprites
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
        #self.rect=pygame.Rect(self.x,self.y,500,50)

    def Render(self,GameWorld):
        #pygame.draw.rect(GameWorld.Screen.window, (255, 0, 0), self.rect, 0)
        #pygame.draw.rect(GameWorld.Screen.window, (255, 255, 255), self.rect, 3)
        pass


def TextOnScreen(Screen,text,text_size,x,y):
        font=pygame.font.SysFont("Britannic Bold", text_size)
        nlabel = font.render(text, 1, (255, 0, 0))
        Screen.window.blit(nlabel, (x, y))

class _StartScreen(object):
    def __init__(self):
        self.Active=True
        self.Screen=_Screen()

    def Processor(self,GameWorld):
        self.Screen.window.fill((0, 0, 0))
        TextOnScreen(self.Screen,"Welcome to the Start Screen, please press 'A' in order to start the game.",30,50,200)
        TextOnScreen(self.Screen,"Welcome to the Start Screen, please press 'A' in order to start the game.",30,50,500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if keyPressed(pygame.K_a):
            self.Active = False
            GameWorld.Active=True


        pygame.display.flip()


class _EndScreen(object):
    def __init__(self,Screen):
        self.Active=True
        self.Screen=Screen

    def Processor(self,GameWorld,processor):
        while self.Active==True:
            self.Screen.window.fill((0, 0, 0))
            #self.GeneralFuncs.TextOnScreen(self.Screen,"Game Over... Rip in Peace",30,50,200)

            #self.GeneralFuncs.TextOnScreen(self.Screen,"Press 'A' in order to restart the game.",30,50,400)
            TextOnScreen(self.Screen, "Game Over... Rip in Peace", 30, 50, 200)
            TextOnScreen(self.Screen, "Your final score is " +str(processor.GameWorld.Player.score), 30, 50, 300)
            TextOnScreen(self.Screen, "Press 'A' in order to restart the game.", 30, 50, 400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if keyPressed(pygame.K_a):
                processor.GameWorld=_GameWorld(processor.Screen,processor)
                processor.GameWorld.Active=True
                self.Active = False


            pygame.display.flip()

class _Processor(object):
    def __init__(self):
        self.Screen=_Screen()
        self.GameWorld=_GameWorld(self.Screen,self)
        self.StartScreen=_StartScreen()
        self.EndScreen=_EndScreen(self.Screen)


        self.CreateNewGameWorld()
        self.CreateStartScreen()
        self.CreateEndScreen()

    def CreateNewGameWorld(self):
        self.GameWorld=_GameWorld(self.Screen,self)

    def CreateStartScreen(self):
        self.StartScreen=_StartScreen()
        self.Screen=self.StartScreen.Screen

    def CreateEndScreen(self):
        self.EndScreen=_EndScreen(self.Screen)

    def EventListener(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()




def main():


    #Player = _Player(300, 410);
    #screen = _Screen();

    #StartScreen=_StartScreen()
    #GameWorld = _GameWorld(StartScreen.Screen)

    Processor=_Processor()

    #_ship = GameWorld.Player.sprite

    y = random.randint(0, 400)

    while 1==1:
        Processor.EventListener()
        if(Processor.StartScreen.Active==True):Processor.StartScreen.Processor(Processor.GameWorld)
        #if(Processor.GameWorld.Active==True): Processor.GameWorld.Processor()
        Processor.GameWorld.Processor()

if __name__ == '__main__':
    main()



