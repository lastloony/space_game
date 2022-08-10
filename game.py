from data import controller
import pygame
from pygame.sprite import Group

from data.gun import Gun
from data.scores import Scores
from data.stats import Stats


def run():
    """
    run game
    :return:
    """

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Первая игра на питоне) Леха, привет!")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controller.create_army(screen, aliens)
    stats = Stats()
    score = Scores(screen, stats)

    while True:
        controller.events(gun, screen, bullets)
        if stats.run_game:
            gun.update_coordinate()
            controller.update(bg_color, screen, gun, bullets, aliens, stats, score)
            controller.update_bullets(bullets, aliens, screen, stats, score)
            controller.update_aliens(stats, screen, gun, aliens, bullets, score)


run()
