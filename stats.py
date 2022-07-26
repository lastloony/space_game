class Stats():
    """Отсвлеживание статистики"""

    def __init__(self):
        self.guns_left = None
        self.reset_stats()

    def reset_stats(self):
        """статистика сброс"""
        self.guns_left = 3
