import pygame
import sys
from bullet import Bullet
from alien import Alien
import sys
from time import sleep
def check_high_score(sb,stats):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,
    ai_settings,screen,sh,sb):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and (not stats.game_active):
        pygame.mouse.set_visible(False)
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, aliens, screen, sh)
        sh.center_ship()
def check_events(stats,play_button,aliens,bullets,ai_settings,screen,sh,sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,sh,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, sh)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets,
            ai_settings, screen, sh,sb)
def check_keydown_events(event,ai_settings,screen,sh,bullets):
    if event.key == pygame.K_ESCAPE:
        sys.exit(0)
    elif event.key == pygame.K_RIGHT:
        sh.moving_right = True
    elif event.key == pygame.K_LEFT:
        sh.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets, ai_settings, screen, sh)
def check_keyup_events(event,sh):
    if event.key == pygame.K_RIGHT:
        sh.moving_right = False
    elif event.key == pygame.K_LEFT:
        sh.moving_left = False
def check_alien_bullet_collison(ai_settings, aliens, screen, sh, bullets, stats, sb):
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collision:
        for num_alien in collision.values():
            stats.score += ai_settings.alien_points * len(num_alien)
            sb.prep_score()
        check_high_score(sb, stats)
    if len(aliens) == 0:
        stats.level += 1
        sb.prep_level()
        bullets.empty()
        ai_settings.increase_speed()
        sb.prep_ships()
        create_fleet(ai_settings, aliens, screen, sh)
def update_bullets(ai_settings, aliens, screen, sh, bullets, stats, sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.top <= 0:
            bullets.remove(bullet)
    check_alien_bullet_collison(ai_settings, aliens, screen, sh, bullets, stats, sb)
def fire_bullets(bullets,ai_settings, screen, sh):
    if len(bullets) <= 5:
        new_bullet = Bullet(ai_settings, screen, sh)
        bullets.add(new_bullet)
def get_number_rows(ai_settings,screen,sh_height,alien_height):
    available_space_y = ai_settings.screen_height - (3*alien_height) - sh_height
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - (2*alien_width)
    available_numaliens_x = int(available_space_x / (2*alien_width))
    return available_numaliens_x
def create_alien(screen,ai_settings,alien_num,aliens,row_num,alien_width,alien_height):
    alien = Alien(screen, ai_settings)
    alien.x = alien_width + (2 * alien_num * alien_width)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * row_num * alien.rect.height)
    aliens.add(alien)
def create_fleet(ai_settings,aliens,screen,sh):
    alien =  Alien(screen,ai_settings)
    num_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    num_row = get_number_rows(ai_settings,screen,sh.rect.height,alien.rect.height)
    for row_num in range(num_row):
        for alien_num in range(num_aliens_x):
            create_alien(screen,ai_settings,alien_num,aliens,row_num,alien.rect.width,alien.rect.height)
def update_screen(ai_settings,screen,sh,bullets,aliens,play_button,stats,sb):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    sh.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
def check_fleet_edges(aliens,ai_settings):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens,ai_settings)
            break
def change_fleet_direction(aliens,ai_settings):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
def ship_hit(aliens, ai_settings, sh, stats, bullets, screen, sb):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, aliens, screen, sh)
        sh.center_ship()
        sleep(0.25)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
def check_aliens_bottom(aliens, ai_settings, sh, stats, bullets, screen, sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(aliens, ai_settings, sh, stats, bullets, screen, sb)
            break
def update_aliens(aliens, ai_settings, sh, stats, bullets, screen, sb):
    check_fleet_edges(aliens,ai_settings)
    aliens.update()
    if pygame.sprite.spritecollideany(sh, aliens):
        ship_hit(aliens, ai_settings, sh, stats, bullets, screen, sb)
    check_aliens_bottom(aliens, ai_settings, sh, stats, bullets, screen, sb)