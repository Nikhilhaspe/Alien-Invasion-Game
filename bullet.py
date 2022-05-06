import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,sh):
        self.screen = screen
        super().__init__()
        self.rect = pygame.Rect(0,0,
            ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = sh.rect.centerx
        self.rect.top = sh.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.bullet_speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        self.y -= self.bullet_speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)