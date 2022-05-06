import pygame.font
class Button():
    def __init__(self,ai_settings,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (255,255,255)
        self.button_color = (0,255,0)
        self.width = 200
        self.height = 50
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)
    def prep_msg(self,msg):
        self.img_msg = self.font.render(msg,True,self.text_color,self.button_color)
        self.rect_img_msg = self.img_msg.get_rect()
        self.rect_img_msg.center = self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.img_msg,self.rect_img_msg)