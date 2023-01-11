from random import randint
from config import *


class Food:
    def __init__(self):
        x = randint(0, (WIDTH_WINDOW/SIZE_SPACE) - 1) * SIZE_SPACE
        y = randint(0, (HEIGHT_WINDOW/SIZE_SPACE) - 1) * SIZE_SPACE
        self.coord = [x, y]

    def create_food(self, canvas):
        canvas.create_rectangle(self.coord[0],
                                self.coord[1],
                                self.coord[0] + SIZE_SPACE,
                                self.coord[1] + SIZE_SPACE,
                                fill=FOOD_COLOR,
                                outline=FIELD_COLOR)

    def is_eating(self, x, y):
        return x == self.coord[0] and y == self.coord[1]

