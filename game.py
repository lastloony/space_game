import sys

from data import controller
from pygame import *
from pygame.sprite import Group

from data.gun import Gun
from data.menu import Menu
from data.scores import Scores
from data.stats import Stats


def run(launched):
    """
    run game
    :return:
    """

    def quit_game():
        global launched
        launched = False

    screen = display.set_mode((700, 800))
    display.set_caption("Первая игра на питоне) Леха, привет!")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controller.create_army(screen, aliens)
    stats = Stats()
    score = Scores(screen, stats)

    while launched:
        # for e in event.get():
        #     if e.type == QUIT:
        #         quit()
        #         launched = False
        #     if e.type == KEYDOWN:
        #         if e.key == K_w or e.key == K_UP:
        #             menu.switch(-1)
        #         elif e.key == K_s or e.key == K_DOWN:
        #             menu.switch(1)
        #         elif e.key == K_SPACE or e.key == K_KP_ENTER:
        #             menu.select()
        #
        # screen.fill((0, 0, 0))
        # menu.draw(screen, 100, 100, 75)
        # display.flip()

        controller.events(gun, screen, bullets)
        if stats.run_game:
            gun.update_coordinate()
            controller.update(bg_color, screen, gun, bullets, aliens, stats, score)
            controller.update_bullets(bullets, aliens, screen, stats, score)
            controller.update_aliens(stats, screen, gun, aliens, bullets, score)


init()
mixer.music.load("data/assets/music/joshua-mclean-mountain-trials.mp3")
mixer.music.play(-1)
menu = Menu()
menu.append_option("Start Game", lambda: print("Start Game"))
# menu.append_option("Exit", quit)
launched = True
run(launched)
