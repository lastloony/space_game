import pygame
import sys
import time

from alien import Alien
from bullet import Bullet


def events(gun, screen, bullets):
    """
    Обработка событий
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.m_right = True
            # влево
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.m_left = True
            # стрельба
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.m_right = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.m_left = False


def update(bg_color, screen, gun, bullets, aliens, stats, score):
    """Обновление экрана"""
    screen.fill(bg_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets, aliens, screen, stats, score):
    """Обновление позиции пули и удаление лишних пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        score.image_score()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


def gun_kill(stats, screen, gun, aliens, bullets):
    """Столконвение пушки и армии"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        aliens.empty()
        bullets.empty()
        gun.create_gun()
        create_army(screen, aliens)
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()


def update_aliens(stats, screen, gun, aliens, bullets):
    """Обновляет позицию пришельцев"""
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, gun, aliens, bullets)
    aliens_check(stats, screen, gun, aliens, bullets)


def aliens_check(stats, screen, gun, aliens, bullets):
    """Проверка добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, aliens, bullets)
            break


def create_army(screen, aliens):
    """Создаем армию пришельцев"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_count_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    alien_count_y_max = int((800 - 100 - 2 * alien_height) / alien_height) - 1
    alien_count_y = 5
    if alien_count_y > alien_count_y_max:
        alien_count_y = alien_count_y_max

    for row in range(alien_count_y):
        for alien_number in range(alien_count_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_height + alien_height * row
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row
            aliens.add(alien)
