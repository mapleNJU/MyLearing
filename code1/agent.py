import numpy as np


class hole():
    def __init__(self, config, x, y):
        self.age = 0
        self.life = np.random.randint(min_life, max_life + 1)
        self.score = np.random.randint(min_score, max_score + 1)
        self.x = x
        self.y = y
