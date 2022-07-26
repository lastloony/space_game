import controller
import pygame
from pygame.sprite import Group

from gun import Gun


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
    while True:
        controller.events(gun, screen, bullets)
        gun.update_coordinate()
        controller.update(bg_color, screen, gun, bullets)
        controller.update_bullets(bullets)


run()
