import pygame
import game_functions as gf
from ship import ship
from settings import settings
from pygame.sprite import Group
from alien import Alien
from Game_Stats import Game_Stats
from button import Button
from scoreboard import Scoreboard
def run_game():
    pygame.init()
    ai_settings = settings()
    stats = Game_Stats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien_invasion")
    bg_color = (ai_settings.bg_color)
    sh = ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    alien = Alien(screen,ai_settings)
    play_button = Button(ai_settings,screen,"Play")
    sb = Scoreboard(stats,screen,ai_settings)
    gf.create_fleet(ai_settings,aliens,screen,sh)
    while True:
        gf.check_events(stats, play_button, aliens, bullets, ai_settings, screen, sh, sb)
        if stats.game_active:
            sh.update()
            gf.update_bullets(ai_settings, aliens, screen, sh, bullets, stats, sb)
            gf.update_aliens(aliens, ai_settings, sh, stats, bullets, screen, sb)
        gf.update_screen(ai_settings,screen,sh,bullets,aliens,play_button,stats,sb)
run_game()