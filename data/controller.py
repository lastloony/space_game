import pygame
import sys

from data.alien import Alien
from settings_game import Settings


def events(gun):
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
            if event.key == pygame.K_SPACE:
                gun.fire = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.m_right = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.m_left = False
            if event.key == pygame.K_SPACE:
                gun.fire = False


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
        check_height_score(stats, score)
        score.image_guns()
    if len(aliens) == 0:
        bullets.empty()
        Settings.level += 1
        create_army(screen, aliens, Settings.level)


def gun_kill(stats, screen, gun, aliens, bullets, score):
    """Столконвение пушки и армии"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        score.image_guns()
        aliens.empty()
        bullets.empty()
        gun.create_gun()
        create_army(screen, aliens, Settings.level)
        pygame.time.delay(200)
    else:
        end_it = False
        while not end_it:
            myfont = pygame.font.SysFont("Britannic Bold", 40)
            nlabel = myfont.render("Game Over", True, (0, 255, 0))
            nlabel_rect = nlabel.get_rect()
            nlabel_rect.centerx = 350
            nlabel_rect.top = 200
            screen.blit(nlabel, nlabel_rect)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    end_it = True
                if event.type == pygame.QUIT:
                    quit()
            pygame.display.flip()
        stats.run_game = False
        sys.exit()


def update_aliens(stats, screen, gun, aliens, bullets, score):
    """Обновляет позицию пришельцев"""
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, gun, aliens, bullets, score)
    aliens_check(stats, screen, gun, aliens, bullets, score)


def aliens_check(stats, screen, gun, aliens, bullets, score):
    """Проверка добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, aliens, bullets, score)
            break


def create_army(screen, aliens, level):
    """Создаем армию пришельцев"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_count_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    alien_count_y_max = int((800 - 100 - 2 * alien_height) / alien_height) - 1
    if level > 5:
        level = 5
    alien_count_y = Settings.row_alien + level  # количество рядов пришельцев
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


def check_height_score(stats, score):
    """Проверка нового рекорда"""
    if stats.score > stats.height_score:
        stats.height_score = stats.score
        score.image_height_score()
        with open("data/score.txt", "w") as f:
            f.write(str(stats.height_score))
