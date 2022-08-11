import pygame

from data import controller
from pygame.sprite import Group

from data.gun import Gun
from data.scores import Scores
from data.stats import Stats
from settings_game import Settings


def run(launched):
    """
    run game
    """

    def quit_game():
        global launched
        launched = False

    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Первая игра на питоне) Леха, привет!")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controller.create_army(screen, aliens, Settings.level)
    stats = Stats()
    score = Scores(screen, stats)

    end_it = False
    while not end_it:
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        nlabel = myfont.render("Start Game", True, (0, 255, 0))
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

    while launched:
        controller.events(gun, screen, bullets)
        if stats.run_game:
            gun.update_coordinate()
            controller.update(bg_color, screen, gun, bullets, aliens, stats, score)
            controller.update_bullets(bullets, aliens, screen, stats, score)
            controller.update_aliens(stats, screen, gun, aliens, bullets, score)


pygame.init()
pygame.mixer.music.load("data/assets/music/joshua-mclean-mountain-trials.mp3")
pygame.mixer.music.play(-1)

launched = True
run(launched)
