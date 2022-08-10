class Stats:
    """Отсвлеживание статистики"""

    def __init__(self):
        self.score = None
        self.guns_left = None
        self.reset_stats()
        self.run_game = True
        with open("score.txt", "r") as f:
            self.height_score = int(f.readline())

    def reset_stats(self):
        """статистика сброс"""
        self.guns_left = 2
        self.score = 0
