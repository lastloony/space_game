class Stats():
    """Отсвлеживание статистики"""

    def __init__(self):
        self.guns_left = None
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """статистика сброс"""
        self.guns_left = 2
