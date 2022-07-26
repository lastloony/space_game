import pygame
import sys
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


def update(bg_color, screen, gun, bullets, aliens):
    """Обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    """Обновление позиции пули и удаление лишних пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_aliens(aliens):
    """Обновляет позицию пришельцев"""
    aliens.update()


def create_army(screen, aliens):
    """Создаем армию пришельцев"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_count_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    alien_count_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row in range(alien_count_y):
        for alien_number in range(alien_count_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_height + alien_height * row
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row
            aliens.add(alien)
