import pygame
from settings_game import Settings


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Создаем пулю в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 2, Settings.bullet_width, 5)  # размер пули
        self.color = 139, 195, 74
        self.speed = Settings.bullet_speed
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
