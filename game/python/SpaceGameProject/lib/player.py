import pygame
import sys
sys.path.insert(0, '/lib')
from lib import funcs
from lib import pygame_textinput


class  _Player(pygame.sprite.Sprite):
    def __init__(self,CurrentProcessor, x, y):
        self.groups = CurrentProcessor.PlayerSprite
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.x=200
        self.y=300
        self.base_speed=5;
        self.bonus_speed=1
        self.main_sprite=pygame.image.load("Sprites/player/ship.png")
        self.LifeIcon=(pygame.transform.rotate(pygame.transform.scale(self.main_sprite,(15,15)),90))
        self.Circle=(pygame.transform.scale(pygame.image.load("Sprites/player/circle.png"),(60,60)))
        self.sprite =pygame.transform.scale(self.main_sprite,(30,30))
        self.width=25+self.sprite.get_width()
        self.heigth=10+self.sprite.get_height()/2
        self.rect= pygame.Rect(self.x,self.y,30,30)
        self.firespeed=0.1
        self.score=0
        self.fuel=100
        self.FuelBar=self.CreateFuelBar()#pygame.Surface((150, 20))
        self.FuelBarRect=self.FuelBar.get_rect(topleft=(10,570))
        self.Life=3
        self.Alpha=255



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

        if(self.Alpha<220):
            if self.y > 375: self.y = 375

        self.rect= pygame.Rect(self.x,self.y,30,30)





    def CreateFuelBar(self):
        _FuelBar = pygame.Surface((150, 20))
        color = (0,255,0)
        # Fill the image with a simple gradient.
        for x in range(_FuelBar.get_width()):
            for y in range(_FuelBar.get_height()):
                _FuelBar.set_at((x, y), color)


        return _FuelBar