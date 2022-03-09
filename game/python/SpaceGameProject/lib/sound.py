import pygame


class _Sounds(object):
    def __init__(self):
        self.StartScreen_music = pygame.mixer.Sound('Sprites/Sound/StartScreen.ogg')
        self.StartScreen_music.set_volume(0.15)
        self.Background_music = pygame.mixer.Sound('Sprites/Sound/Background.ogg')
        self.Background_music.set_volume(0.05)
        self.PlayerDeath_sound = pygame.mixer.Sound('Sprites/Sound/PlayerDeath.wav')
        self.PlayerLaser_sound=pygame.mixer.Sound('Sprites/Sound/PlayerLaser.ogg')
        self.PlayerLaser_sound.set_volume(0.5)
        self.PlayerRocket_sound=pygame.mixer.Sound('Sprites/Sound/PlayerRocket.wav')
        self.PlayerRocket_sound.set_volume(0.05)
        self.PlayerNoRocket_sound=pygame.mixer.Sound('Sprites/Sound/PlayerNoRocket.wav')


    def StopAllSounds(self):
        pygame.mixer.Sound.stop(self.StartScreen_music)
        pygame.mixer.Sound.stop(self.Background_music)