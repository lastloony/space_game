import controller
import pygame


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
    while True:
        controller.events(gun)
        gun.update_coordinate()
        controller.update(bg_color, screen, gun)


run()
