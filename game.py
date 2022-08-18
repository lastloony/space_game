import pygame

from data import controller
from pygame.sprite import Group

from data.bullet import Bullet
from data.gun import Gun
from data.scores import Scores
from data.stats import Stats
from settings_game import Settings


def run(launched, clock):
    """
    run game
    """
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Первая игра на питоне")
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

    leha_hi = True
    while leha_hi:
        screen.fill(bg_color)
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        nlabel = myfont.render("Леха привет!", True, (0, 255, 0))
        nlabel_rect = nlabel.get_rect()
        nlabel_rect.centerx = 350
        nlabel_rect.top = 100
        screen.blit(nlabel, nlabel_rect)
        image = pygame.image.load("data/assets/img.png")
        rect = image.get_rect()
        rect.centerx = 350
        rect.bottom = 500
        screen.blit(image, rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                leha_hi = False
            if event.type == pygame.QUIT:
                quit()
        pygame.display.flip()
    dt = 0
    while launched:
        controller.events(gun)
        if stats.run_game:
            gun.update_coordinate()
            controller.update(bg_color, screen, gun, bullets, aliens, stats, score)
            controller.update_bullets(bullets, aliens, screen, stats, score)
            controller.update_aliens(stats, screen, gun, aliens, bullets, score)
            dt += 1
            if gun.fire and dt > 10:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                dt = 0

        clock.tick(60)


pygame.init()
pygame.mixer.music.load("data/assets/music/joshua-mclean-mountain-trials.mp3")
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()

launched = True
run(launched, clock)
