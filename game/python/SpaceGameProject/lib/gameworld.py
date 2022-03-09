import pygame
import time
import random
import sys
sys.path.insert(0, '/lib')
from lib import objects
from lib import funcs
from lib import pygame_textinput

class _GameWorld:
    def __init__(self,CurrentProcessor):
        self.Sprites=CurrentProcessor.Sprites
        self.CurrentProcessor=CurrentProcessor
        self.GameTime = time.time()
        self.Player_last_fire = time.time()
        self.Player_last_rocket=time.time()
        self.Enemy_last_spawn = time.time()
        self.Fuel_last_update=time.time()
        #self.Enemies = []
        #self.Bullets = []
        self.Screen=CurrentProcessor.Screen
        #self.Level=Level
        self.Player=CurrentProcessor.Player
        self.GameWorldScore=0
        self.Active=True
        self.Paused=False
        self.Initialized=False
        self.LastGameStop=time.time()


    def newWorld(self):
        pass

    def GenerateWorld(self,GroundAmount):
        for x in range(0,GroundAmount-1):
            SpawnY=random.randint(400,600)
            CreatedRock = objects.Rock(self.CurrentProcessor, x*500, SpawnY)
            PosY=0
            GrassYSub=(random.randint(30,50))
            objects.Grass(self.CurrentProcessor, x*500, SpawnY-GrassYSub)
            if x>3:
                for a in range(0,random.randint(1,5)):
                    if(a==0): PosY=6
                    elif(a==1): PosY=2
                    elif(a==2):PosY=7
                    elif(a==3): PosY=2
                    elif(a==4):PosY=-4
                    # self.Sprites.EnemySprites.add(_EnemyRocket(self.CurrentProcessor, 50, 200,2.5, self.Player))
                    objects._EnemyRocket(self.CurrentProcessor, CreatedRock.x+a*109, CreatedRock.y-5+PosY-GrassYSub,2.5+self.CurrentProcessor.Difficulity*1+(self.CurrentProcessor.Level*0.2))
                    #self.Sprites.EnemySprites.add(_EnemyRocket(self.CurrentProcessor, x*500+a*109,CreatedRock.y-20, 2.5))
                    if(random.randint(1,3)==1):
                        objects._FuelBarrel(self.CurrentProcessor,CreatedRock.x+a*109+43, CreatedRock.y-5+PosY-GrassYSub, 2.5, CreatedRock)

    def EventListener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        if funcs.keyPressed(pygame.K_ESCAPE):
            if (self.Paused == False and self.GameRealTime-self.LastGameStop>0.2):
                self.LastGameStop=time.time()
                self.Paused = True
            elif(self.Paused == True and self.GameRealTime-self.LastGameStop>0.2):
                self.LastGameStop=time.time()
                self.Paused = False

        #Player Events while game is active
        if(self.Active==True and self.Paused==False):
            if funcs.keyPressed(pygame.K_LEFT): self.Player.move("left")
            if funcs.keyPressed(pygame.K_RIGHT): self.Player.move("right")
            if funcs.keyPressed(pygame.K_UP): self.Player.move("up")
            if funcs.keyPressed(pygame.K_DOWN): self.Player.move("down")
            if funcs.keyPressed(pygame.K_v):self.CreateNewBullet("Rocket")
            if funcs.keyPressed(pygame.K_SPACE): self.CreateNewBullet("Laser")

            if funcs.keyPressed(pygame.K_r):
                self.PlayerDeath()







    def CreateNewBullet(self,text):
        #self.GameTime = time.time()
        if(text=="Laser"):
            if len(self.Sprites.BulletSprites) < 25 and ((self.GameTime - self.Player_last_fire) > (0.3 - self.Player.firespeed)):
                self.Player_last_fire = time.time()
                self.Sprites.BulletSprites.add(objects.SingleBullet(self.CurrentProcessor,(round(self.Player.x + self.Player.width // 2)), (round(self.Player.y + self.Player.heigth // 2)),self.Player.base_speed, 1))
                pygame.mixer.Sound.play(self.CurrentProcessor.Sounds.PlayerLaser_sound)

        elif(text=="Rocket"):
            if len(self.Sprites.RocketSprites) < 3 and ((self.GameTime - self.Player_last_rocket) > (0.4 - self.Player.firespeed)):
                self.Player_last_rocket = time.time()
                self.Sprites.BulletSprites.add(objects.SingleRocket(self.CurrentProcessor,(round(self.Player.x + self.Player.width // 2)), (round(self.Player.y + self.Player.heigth // 2)),self.Player.base_speed, 3))
                pygame.mixer.Sound.play(self.CurrentProcessor.Sounds.PlayerRocket_sound)


    def CreateEnemy(self):
        if len(self.Sprites.EnemyUFOs)+len(self.Sprites.EnemySHIPs)<7:
            if ((self.GameTime - self.Enemy_last_spawn) > 1):
                self.Enemy_last_spawn = time.time()
                if(random.randint(1,15+(self.CurrentProcessor.Difficulity))<13):
                        #self.Enemies.append(_Enemy(self,750,random.randint(20,500),2.5))
                        self.Sprites.EnemySprites.add(objects._Enemy(self.CurrentProcessor, 805, random.randint(10, 380), 3+(self.CurrentProcessor.Difficulity*1+self.CurrentProcessor.Level*0.2)))

                else:
                    self.Sprites.EnemySprites.add(objects._EnemyUFO(self.CurrentProcessor, 805, random.randint(20, 350), 2 + (
                                self.CurrentProcessor.Difficulity * 1 + self.CurrentProcessor.Level * 0.2)))

    def RenderSprites(self):

        for sprite in self.Sprites.GroundSprites:
            if sprite.x<200000 and sprite.x>-500:
                self.Screen.window.blit(sprite.sprite,(sprite.x, sprite.y))
                #pygame.draw.rect(self.Screen.window, (255, 0, 0), sprite.rect, 2)
            else:
                sprite.kill()

        for sprite in self.Sprites.AllSprites:
            if sprite.x<200000 and sprite.x>-20:
                self.Screen.window.blit(sprite.sprite,(sprite.x, sprite.y))
                #pygame.draw.rect(self.Screen.window, (255, 0, 0), sprite.rect, 2)
            else:
                sprite.kill()



        #self.Screen.window.blit(self.CurrentProcessor.Player.sprite,(self.CurrentProcessor.Player.x,self.CurrentProcessor.Player.y))
        if(self.Player.Alpha<220):
            self.Screen.window.blit(self.Player.Circle, (self.CurrentProcessor.Player.x-15, self.CurrentProcessor.Player.y-15))

        self.Screen.Blit_Alpha(self.Screen.window,self.CurrentProcessor.Player.sprite,
                                (self.CurrentProcessor.Player.x, self.CurrentProcessor.Player.y),self.CurrentProcessor.Player.Alpha)
        if self.Player.Life>0:
            for x in range(0,self.Player.Life):
                self.Screen.window.blit(self.CurrentProcessor.Player.LifeIcon,(20+x*20,540))

        #self.Player.LI.set_alpha(0)
        #self.Screen.window.blit(self.Player.LI,(300,550))
        #self.Screen.Blit_Alpha(self.Screen.window,self.Player.LI,(300,500),20)




    #def RenderPlayerLifeAmount(self):
        #self.Screen.window.blit(self.CurrentProcessor.Player.LifeIcon,(20,540))

    def PlayerDeath(self):
        self.Active = False
        #EndScreen = _EndScreen(self.Screen)
        #print (len(self.CurrentProcessor.ScoreBoardPoints))
        for a in range(1,len(self.CurrentProcessor.ScoreBoardPoints)+1,1):
            if(self.CurrentProcessor.Player.score>int(self.CurrentProcessor.ScoreBoardPoints[a-1])):
                #print (len(self.CurrentProcessor.ScoreBoardPoints))
                self.CurrentProcessor.Scenes.UpdateScores(a-1,self.Player.score)
                break

        self.CurrentProcessor.Scenes.EndScreen()
        #self.CurrentProcessor.EndScreen.Processor(self.CurrentProcessor)

    def EnemyDeath(self,Enemy):
        self.Player.score +=round(Enemy.ScoreBonus*((self.CurrentProcessor.Difficulity*0.5+self.CurrentProcessor.Level*0.2)))
        self.GameWorldScore+=round(Enemy.ScoreBonus*((self.CurrentProcessor.Difficulity*0.5+self.CurrentProcessor.Level*0.2)))

    def ObjectDeath(self,Object):
        self.Player.score +=round(Object.ScoreBonus*((self.CurrentProcessor.Difficulity*0.5+self.CurrentProcessor.Level*0.2)))
        self.GameWorldScore+=round(Object.ScoreBonus*((self.CurrentProcessor.Difficulity*0.5+self.CurrentProcessor.Level*0.2)))
        self.Player.fuel += Object.FuelBonus

    def RefreshPlayer(self):
        self.Player.Alpha=30
        self.CurrentProcessor.Player.fuel=100
        self.CurrentProcessor.Player.Life=3
        self.CurrentProcessor.Player.score=0

    def RefreshPlayerPos(self):
        self.Player.x=50
        self.Player.y=200

    def RenderFuel(self):
        self.Screen.window.blit(self.Player.FuelBar, self.Player.FuelBarRect,(0, 0, self.Player.FuelBarRect.w / 100 * self.Player.fuel, self.Player.FuelBarRect.h))
        pygame.draw.rect(self.Screen.window,(0,255,255),(10,570,149,21),1)
        funcs.TextOnScreen(self.Screen,"FUEL",20,70,575)

    def FuelEvents(self,AddedAmount):
        #self.Player.fuel -= 1  # Reduce the heat every frame.
        self.Player.fuel +=AddedAmount;
        self.Player.fuel = max(1, min(self.Player.fuel, 100))  # Clamp the value between 1 and 100.
        self.Fuel_last_update = self.GameTime



    def Initialize(self):
        self.Screen.window.fill((0, 0, 0))
        self.CurrentProcessor.Sounds.StopAllSounds()

        pygame.mixer.Sound.play(self.CurrentProcessor.Sounds.Background_music,-1)
        funcs.TextOnScreen(self.Screen, "Initializing... Level: "+str(self.CurrentProcessor.Level)+", Difficulity: "+self.CurrentProcessor.DifficulityName, 30, 50, 200)
        pygame.display.update()
        pygame.display.flip();
        self.Player.x=50
        self.Player.y=200
        self.GenerateWorld(50)
        self.Player.Alpha=50
        self.Initialized=True



    def CheckColliders(self):
        # self.Screen.window.blit(self.Player.FuelBarRect,(0, 0, self.Player.FuelBarRect.w / 100 * self.Player.fuel, self.Player.FuelBarRect.h))

        # if(pygame.sprite.groupcollide(self.BulletSprites, self.EnemySprites, True, True)): self.EnemyDeath()
        hits = (pygame.sprite.groupcollide(self.Sprites.BulletSprites, self.Sprites.EnemySprites, True, True))
        for bullets in hits:
            for Enemy in hits[bullets]:
                self.EnemyDeath(Enemy)
        hits = (pygame.sprite.groupcollide(self.Sprites.BulletSprites, self.Sprites.ObjectSprites, True, True))
        for bullets in hits:
            for Object in hits[bullets]:
                self.ObjectDeath(Object)


        pygame.sprite.groupcollide(self.Sprites.BulletSprites, self.Sprites.GroundSprites, True, False)

        if(self.Player.Alpha>220):
            if pygame.sprite.groupcollide(self.CurrentProcessor.PlayerSprite, self.Sprites.EnemySprites, False, True):
                #pygame.mixer.Sound.play(self.CurrentProcessor.Sounds.PlayerDeath_sound)
                if self.Player.Life>0:
                    self.Player.Life-=1
                    self.Player.Alpha = 30
                    self.RefreshPlayerPos()
                else: self.PlayerDeath()

            if pygame.sprite.groupcollide(self.CurrentProcessor.PlayerSprite, self.Sprites.GroundSprites, False,
                                          False):
                #pygame.mixer.Sound.play(self.CurrentProcessor.Sounds.PlayerDeath_sound)
                if self.Player.Life > 0:
                    self.Player.Life -= 1
                    self.Player.Alpha = 30
                    self.RefreshPlayerPos()
                else: self.PlayerDeath()
        #pygame.sprite.groupcollide(self.Sprites.EnemyUFOs,self.Sprites.GroundSprites,True,False)
        # pygame.sprite.groupcollide(GameWorld.EnemySprites,GameWorld.GroundSprites,True,False)


    def CheckPlayerState(self):
        if self.GameWorldScore>2000+(self.CurrentProcessor.Level-1)*500:
            self.CurrentProcessor.Level+=1
            self.CurrentProcessor.GameWorld=self.CurrentProcessor.CreateNewGameWorld()
        if self.Player.fuel <= 1: self.PlayerDeath()
        if ((self.GameTime - self.Fuel_last_update) > 1): self.FuelEvents(-1)

        self.Player.Alpha +=1;
        self.Player.Alpha = max(1, min(self.Player.Alpha, 255))  # Clamp the value between 1 and 100.

    def Processor(self):
        self.EventListener()
        self.GameRealTime = time.time()
        if (self.Active == True):
            if(self.Paused==False):
                if(self.Initialized==False): self.Initialize()

                for rock in self.Sprites.GroundSprites:
                    rock.move()
                    #rock.Render(self)


                self.Screen.renderBg();
                self.Screen.BgMovement();


                #TextOnScreen(self.Screen, "Your Score: " + str(self.GameTime-self.Fuel_last_update), 50, 255, 255)



                self.CheckPlayerState()


                for bullet in self.Sprites.BulletSprites:
                    bullet.move()

                # GameWorld.GenerateGround()



                for enemy in self.Sprites.EnemySprites:
                    enemy.move()
                    # enemy.render(GameWorld.Screen.window);

                for object in self.Sprites.ObjectSprites:
                    object.move()

                self.RenderSprites()

                self.CreateEnemy()

                funcs.TextOnScreen(self.Screen, "Your Score: "+str(self.Player.score), 30, 170, 570)
                self.RenderFuel()

                self.CheckColliders()

                pygame.display.update()
                pygame.display.flip();

                self.GameTime = time.time()
                self.Screen.clock.tick(60)
                # GameWorld.Player.render(GameWorld.Screen.window);
            else:
                funcs.TextOnScreen(self.Screen, "Game Stopped!", 50, 300, 260)
                pygame.display.flip();

                self.Screen.clock.tick(60)
        #elif(self.CurrentProcessor.StartScreen.Active==False):
