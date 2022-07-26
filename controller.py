import pygame
import sys
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


def update(bg_color, screen, gun, bullets):
    """Обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()


def update_bullets(bullets):
    """Обновление позиции пули и удаление лишних пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
