import pygame


class Scores:
    """Вывод очков"""

    def __init__(self, screen, stats):
        """Инициализируем подсчет очков"""
        self.score_rect = None
        self.score_img = None
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
    
    def image_score(self):
        """Преобразовывает текст счета в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
