import pygame
from pygame.sprite import Group
from data.gun import Gun


class Scores:
    """Вывод очков"""

    def __init__(self, screen, stats):
        """Инициализируем подсчет очков"""
        self.lives = None
        self.score_rect = None
        self.score_img = None
        self.height_score_rect = None
        self.height_score_img = None
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_height_score()
        self.image_guns()
    
    def image_score(self):
        """Преобразовывает текст счета в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_height_score(self):
        """Преобразовывает рекорд счета в графическое изображение"""
        self.height_score_img = self.font.render(str(self.stats.height_score), True, self.text_color, (0, 0, 0))
        self.height_score_rect = self.score_img.get_rect()
        self.height_score_rect.centerx = self.screen_rect.centerx
        self.height_score_rect.top = 20

    def image_guns(self):
        """Количество жизней"""
        self.lives = Group()
        for live_number in range(self.stats.guns_left):
            live = Gun(self.screen)
            live.rect.x = 15 + live_number * live.rect.width
            live.rect.y = 20
            self.lives.add(live)

    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.height_score_img, self.height_score_rect)
        self.lives.draw(self.screen)
