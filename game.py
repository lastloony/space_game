import controller
import pygame
from pygame.sprite import Group

from gun import Gun
from stats import Stats


def run():
    """
    run game
    :return:
    """

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Первая игра на питоне)")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controller.create_army(screen, aliens)
    stats = Stats()

    while True:
        controller.events(gun, screen, bullets)
        gun.update_coordinate()
        controller.update(bg_color, screen, gun, bullets, aliens)
        controller.update_bullets(bullets, aliens, screen)
        controller.update_aliens(stats, screen, gun, aliens, bullets)


run()
