import pygame


class _Sprites(object):
    def __init__(self):
        self.AllSprites = pygame.sprite.Group()
        self.GroundSprites = pygame.sprite.Group()
        self.EnemySprites = pygame.sprite.Group()
        self.BulletSprites = pygame.sprite.Group()
        self.RocketSprites = pygame.sprite.Group()
        self.EnemySHIPs = pygame.sprite.Group()
        self.EnemyUFOs = pygame.sprite.Group()
        self.EnemyROCKETs = pygame.sprite.Group()
        self.ObjectSprites = pygame.sprite.Group()