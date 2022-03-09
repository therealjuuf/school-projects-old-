import pygame
import csv
import sys
sys.path.insert(0, '/lib')
from lib import scenes
from lib import player
from lib import sprites
from lib import gameworld
from lib import sound

class _Processor(object):
    def __init__(self):
        self.Screen=scenes._Screen()
        self.Sprites=sprites._Sprites()
        self.PlayerSprite = pygame.sprite.Group()
        self.Player= player._Player(self,300, 410);
        self.GameWorld=self.CreateNewGameWorld()
        self.Scenes=scenes._Scenes(self)
        self.Sounds=sound._Sounds()
        self.ScoreBoardNames=[]
        self.ScoreBoardPoints=[]
        self.Level=1
        self.Difficulity=1
        self.DifficulityName="Easy"
        self.Score=0
        self.ReadScores()

    def CreateNewGameWorld(self):
        self.Sprites=sprites._Sprites()
        GameWorld=gameworld._GameWorld(self)
        return GameWorld


    def EventListener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def ReadScores(self):
        with open('scores.txt') as csvDataFile:
            csvReader = csv.DictReader(csvDataFile, delimiter=',', quotechar='"', escapechar=' ')
            for row in csvReader:
                self.ScoreBoardNames.append(row["name"])
                self.ScoreBoardPoints.append(row["point"])
        csvDataFile.close()
        print(self.ScoreBoardPoints)
        print(len(self.ScoreBoardPoints))

    def SaveScores(self):
        with open('scores.txt','w') as csvDataFile2:
            fieldnames=['name','point']
            csvWriter = csv.DictWriter(csvDataFile2, fieldnames=fieldnames)
            csvWriter.writeheader()
            print (len(self.ScoreBoardPoints))
            a = 0
            for player in self.ScoreBoardNames:
                csvWriter.writerow({'name':self.ScoreBoardNames[a], 'point':self.ScoreBoardPoints[a]})
                a += 1
            #print (len(self.ScoreBoardPoints))
        csvDataFile2.close()





def main():


    #Player = _Player(300, 410);
    #screen = _Screen();

    #StartScreen=_StartScreen()
    #GameWorld = _GameWorld(StartScreen.Screen)

    Processor=_Processor()

    #pygame.mixer.music.play(-1)
    Processor.Scenes.StartScreen()

    #_ship = GameWorld.Player.sprite

    #y = random.randint(0, 400)

    while 1==1:
        Processor.EventListener()
        #if(Processor.StartScreen.Active==True):Processor.StartScreen.Processor(Processor)
        #if(Processor.GameWorld.Active==True): Processor.GameWorld.Processor()
        Processor.GameWorld.Processor()

if __name__ == '__main__':
    main()



