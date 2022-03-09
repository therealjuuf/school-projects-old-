import pygame
import csv
import sys
sys.path.insert(0, '/lib')
from lib import pygame_textinput



Player=[]
Points=[]


def ReadScore():
    with open('scores.txt') as csvDataFile:
        csvReader = csv.DictReader(csvDataFile,delimiter=',',quotechar='"', escapechar=' ')
        for row in csvReader:
            Player.append(row["name"])
            Points.append(row["point"])

    csvDataFile.close()
    return (Player)

def SaveScore():
    with open('scores.txt','w') as csvDataFile2:
        fieldnames=['name','point']
        csvWriter = csv.DictWriter(csvDataFile2, fieldnames=fieldnames)
        a=0
        csvWriter.writeheader()
        for player in Player:
            csvWriter.writerow({'name':Player[a], 'point':Points[a]})
            a+=1
    csvDataFile2.close()

def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False





pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInput()
name='0'
screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()
isTakingName=True
ReadScore()






while True:
    screen.fill((225, 225, 225))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    #if keyPressed(pygame.K_KP_ENTER):
    #    isTakingName=False

    # Feed it with events every frame
    #textinput.update(events)
    if isTakingName==True:
        if textinput.update(events):
            name=textinput.get_text()
            Player[1]=name
            SaveScore()
            isTakingName=False
            #print(textinput.get_text())
        # Blit its surface onto the screen
        #print (name)
        screen.blit(textinput.get_surface(), (10, 10))



    pygame.display.update()
    clock.tick(30)