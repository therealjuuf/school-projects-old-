import pygame


def TextOnScreen(Screen, text, text_size, x, y):
    font = pygame.font.SysFont("Britannic Bold", text_size)
    nlabel = font.render(text, 1, (255, 0, 0))
    Screen.window.blit(nlabel, (x, y))

def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False