import sys
import pygame
import time
import random

class  _Player(object):
    def __init__(self, x, y):
        self.posx=200
        self.posy=300
        self.base_speed=5;
        self.bonus_speed=1
        self.main_sprite=pygame.image.load("Sprites/player/ship.png")
        self.ship =pygame.transform.scale(self.main_sprite,(30,30))
        self.width=25+self.ship.get_width()
        self.heigth=10+self.ship.get_height()/2
        self.hitbox= (self.posx,self.posy,30,30)
        self.firespeed=0.1
        self.score=0
        self.fuel=100

    def render(self,window):
        window.blit(self.ship, (self.posx, self.posy));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def move(self,pos):
        if (pos=="right"):
            self.posx += self.base_speed*self.bonus_speed
        elif (pos == "left"):
            self.posx -= self.base_speed*self.bonus_speed;
        elif(pos=="up"):
            self.posy -=self.base_speed*self.bonus_speed;
        elif(pos=="down"):
            self.posy +=self.base_speed*self.bonus_speed;
        if self.posx>750: self.posx=750
        if self.posx<0: self.posx=0
        if self.posy>590: self.posy=590
        if self.posy<10: self.posy=10
        self.hitbox= (self.posx,self.posy,30,30)

class SingleBullet(object):
    def __init__(self,x,y,player_base_speed,bonus_vel):
        self.x=x
        self.y=y
        self.velocity=bonus_vel+player_base_speed
        self.sprite = pygame.transform.scale(pygame.image.load("Sprites/player/SingleLaser.png"),(10,4))
        self.hitbox=(self.x,self.y,10,4);

    def move(self):
        self.x+=self.velocity
        self.hitbox=(self.x,self.y,10,4)

    def render(self,window):
        window.blit(self.sprite, (self.x, self.y));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

class _Enemy(object):
    def __init__(self,x,y,velocity):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.sprite= pygame.transform.scale(pygame.image.load("Sprites/enemy/enemy1.png"),(30,30))
        self.hitbox= (self.x,self.y,30,30)

    def move(self):
        self.x-=self.velocity
        self.hitbox = (self.x, self.y, 30, 30)

    def render(self,window):
        window.blit(self.sprite, (self.x, self.y));
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)


class _Screen(object):
    def __init__(self):
        self.resolution=(800, 600)
        self.window=pygame.display.set_mode(self.resolution)
        self.bg=(pygame.transform.scale(pygame.image.load("Sprites/Bg/darkPurple.png"),self.resolution))
        self.bgWidth=self.bg.get_width()
        self.bgPosX1=0
        self.bgPosX2=self.bgWidth
        pygame.mouse.set_visible(0)

    def getGameWindow(self):
        return pygame.display.set_mode(self.resolution)

    def renderBg(self):
        self.window.blit(self.bg,(self.bgPosX1,0));
        self.window.blit(self.bg,(self.bgPosX2,0))



def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False





bullets=[]
enemies=[]



def main():
    pygame.init()

    player = _Player(300, 410);
    screen = _Screen();

    clock = pygame.time.Clock()

    _ship = player.ship
    last_fire=time.time()
    last_spawn = time.time()
    enemy = _Enemy(500,500,4)

    while 1==1:

        screen.renderBg();
        screen.bgPosX1 -=1.4;
        screen.bgPosX2 -= 1.4;
        if screen.bgPosX1 < screen.bgWidth*-1:
            screen.bgPosX1 = screen.bgWidth
        if screen.bgPosX2<screen.bgWidth*-1:
            screen.bgPosX2 = screen.bgWidth




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        for bullet in bullets:
            if bullet.x<800 and bullet.x>0:
                bullet.move()
                bullet.render(screen.window);
                for enemy in enemies:
                    if bullet.y-bullet.hitbox[3] < enemy.hitbox[1]+enemy.hitbox[3] and bullet.y + bullet.hitbox[3] > enemy.hitbox[1]:
                        if bullet.x + bullet.hitbox[3] > enemy.hitbox[0] and bullet.x - bullet.hitbox[3] < enemy.hitbox[0] + enemy.hitbox[2]:
                            bullets.pop(bullets.index(bullet))
                            enemies.pop(enemies.index(enemy))
            else:
                bullets.pop(bullets.index(bullet))

        for enemy in enemies:
            if enemy.x<800 and enemy.x>0:
                enemy.move()
                enemy.render(screen.window);
            else:
                enemies.pop(enemies.index(enemy))

        if keyPressed(pygame.K_LEFT): player.move("left")
        if keyPressed(pygame.K_RIGHT): player.move("right")
        if keyPressed(pygame.K_UP): player.move("up")
        if keyPressed(pygame.K_DOWN): player.move("down")
        if keyPressed(pygame.K_SPACE):
            now = time.time()
            if len(bullets)<25 and ((now-last_fire)>(0.3 - player.firespeed)):

                last_fire = time.time()
                bullets.append(SingleBullet(round(player.posx+player.width//2),(round(player.posy+player.heigth//2)),player.base_speed,1))

        if len(enemies)<7:
            now = time.time()
            if ((now-last_spawn)>1):
                last_spawn = time.time()
                enemies.append(_Enemy(750,random.randint(20,500),2.5))


        player.render(screen.window);
        pygame.display.update()
        pygame.display.flip();


        clock.tick(60)



if __name__ == '__main__':
    main()







