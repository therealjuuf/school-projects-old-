import pygame
import sys
sys.path.insert(0, '/lib')
from lib import funcs
from lib import pygame_textinput


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


    def Blit_Alpha(self,target,source,location,opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        target.blit(temp, location)




class _Scenes(object):
    def __init__(self,CurrentProcessor):
        self.CurrentProcessor=CurrentProcessor

    def Scoreboard(self):
        isShowingScoreBoard = True
        while isShowingScoreBoard == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if funcs.keyPressed(pygame.K_a):
                self.CurrentProcessor.Scenes.StartScreen()
                isShowingScoreBoard = False

            self.CurrentProcessor.Screen.window.fill((225, 225, 225))
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Press A to go back to start screen.", 30, 50, 100)


            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Name", 30, 50, 200)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Score", 30, 200, 200)
            for a in range(0, 10):
                funcs.TextOnScreen(self.CurrentProcessor.Screen, str(a + 1) + '. ' + str(self.CurrentProcessor.ScoreBoardNames[a]), 30,
                             50, 220 + a * 20)
                funcs.TextOnScreen(self.CurrentProcessor.Screen,str(self.CurrentProcessor.ScoreBoardPoints[a]), 30, 200,220 + a * 20)
            pygame.display.update()
            pygame.display.flip()

    def UpdateScores(self, Position, Score):
        textinput = pygame_textinput.TextInput()
        isTakingName = True
        TookName = True
        while isTakingName == True:
            events = pygame.event.get()
            if textinput.update(events):
                isTakingName = False
                name = textinput.get_text()
                if name is None: name = "BlankName"
                for x in range(9,Position,-1):
                    self.CurrentProcessor.ScoreBoardPoints[x]=self.CurrentProcessor.ScoreBoardPoints[x-1]
                    self.CurrentProcessor.ScoreBoardNames[x] = self.CurrentProcessor.ScoreBoardNames[x-1]
                self.CurrentProcessor.ScoreBoardPoints[Position] = Score
                self.CurrentProcessor.ScoreBoardNames[Position] = name
                self.CurrentProcessor.SaveScores()

                # print(textinput.get_text())
            # Blit its surface onto the screen
            # print (name)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Congrats! You have successfully beaten a player.", 30, 170, 225)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Please enter your name below. ", 30, 250, 250)
            pygame.draw.rect(self.CurrentProcessor.Screen.window, (225, 225, 225), (200, 280, 400, 60), 0)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Name: ", 35, 225, 300)
            self.CurrentProcessor.Screen.window.blit(textinput.get_surface(), (300, 300))

            pygame.display.update()
            pygame.display.flip()

    def EndScreen(self):
        isEndScreen=True
        self.CurrentProcessor.Sounds.StopAllSounds()
        while isEndScreen == True:
            # self.Screen.window.set_alpha(255)
            self.CurrentProcessor.Screen.window.fill((225, 225, 225))

            # self.GeneralFuncs.TextOnScreen(self.Screen,"Game Over... Rip in Peace",30,50,200)

            # self.GeneralFuncs.TextOnScreen(self.Screen,"Press 'A' in order to restart the game.",30,50,400)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Game Over... Rip in Peace", 30, 50, 200)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Your final score is " + str(self.CurrentProcessor.GameWorld.Player.score), 30, 50,
                         300)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Press L to see leaderboard.", 30, 50, 400)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Press 'A' in order to restart the game.", 30, 50, 450)

            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Press 'S' in order to restart the game.", 30, 50, 500)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if funcs.keyPressed(pygame.K_a):
                self.CurrentProcessor.Level = 1
                self.CurrentProcessor.GameWorld = self.CurrentProcessor.CreateNewGameWorld()
                self.CurrentProcessor.GameWorld.RefreshPlayer()
                self.CurrentProcessor.GameWorld.Active = True
                isEndScreen = False

            if funcs.keyPressed(pygame.K_s):
                self.CurrentProcessor.Level = 1
                self.CurrentProcessor.GameWorld.RefreshPlayer()
                isEndScreen = False
                self.CurrentProcessor.Scenes.StartScreen()

            if funcs.keyPressed(pygame.K_l):
                isEndScreen = False
                self.Scoreboard()


            pygame.display.flip()

    def StartScreen(self):
        isStartScreen=True
        self.CurrentProcessor.Sounds.StopAllSounds()
        pygame.mixer.Sound.play(self.CurrentProcessor.Sounds.StartScreen_music, -1)
        while isStartScreen==True:
            self.CurrentProcessor.GameWorld.Active = False
            self.CurrentProcessor.Screen.window.fill((225, 225, 225))
            # TextOnScreen(self.Screen,"Welcome to the Start Screen, please press 'A' in order to start the game.",30,50,200)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Welcome to ETERNAL SCRAMBLE ARCADE!", 30, 50, 100)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Press L to see leaderboard.", 30, 50, 350)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Press F1 to start game in Easy Mode", 30, 50, 400)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Press F2 to start game in Normal Mode", 30, 50, 450)
            funcs.TextOnScreen(self.CurrentProcessor.Screen, "Press F3 to start game in Hard Mode", 30, 50, 500)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if funcs.keyPressed(pygame.K_l):
                isEndScreen = False
                self.Scoreboard()

            if funcs.keyPressed(pygame.K_F1):
                isStartScreen = False
                self.CurrentProcessor.Difficulity = 1
                self.CurrentProcessor.DifficulityName = "Easy"
                self.CurrentProcessor.Score = 0
                self.CurrentProcessor.GameWorld.RefreshPlayer()
                self.CurrentProcessor.GameWorld = self.CurrentProcessor.CreateNewGameWorld()
            elif funcs.keyPressed(pygame.K_F2):
                isStartScreen = False
                self.CurrentProcessor.DifficulityName = "Normal"
                self.CurrentProcessor.Difficulity = 2
                self.CurrentProcessor.Score = 0
                self.CurrentProcessor.GameWorld.RefreshPlayer()
                self.CurrentProcessor.GameWorld = self.CurrentProcessor.CreateNewGameWorld()
            elif funcs.keyPressed(pygame.K_F3):
                isStartScreen = False
                self.CurrentProcessor.DifficulityName = "Hard"
                self.CurrentProcessor.Difficulity = 3
                self.CurrentProcessor.Score = 0
                self.CurrentProcessor.GameWorld.RefreshPlayer()
                self.CurrentProcessor.GameWorld = self.CurrentProcessor.CreateNewGameWorld()

            pygame.display.flip()