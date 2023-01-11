from config import *
SNAKE_LEN = 2


class Snake:
    def __init__(self):
        self.__direction = 'down'
        self.snake_length = SNAKE_LEN
        self.coord = [[0, 0]] * SNAKE_LEN
        self.body_parts = []

    def create_snake(self, canvas):
        for x, y in self.coord:
            body_part = canvas.create_rectangle(x, y, x + SIZE_SPACE, y + SIZE_SPACE, fill=BODY_COLOR, outline=FIELD_COLOR)
            self.body_parts.append(body_part)

    def set_direction(self, direction):
        if direction == 'down':
            if self.__direction != 'up':
                self.__direction = direction
        elif direction == 'up':
            if self.__direction != 'down':
                self.__direction = direction
        elif direction == 'left':
            if self.__direction != 'right':
                self.__direction = direction
        elif direction == 'right':
            if self.__direction != 'left':
                self.__direction = direction

    def check_snake_crash(self):
        x, y = self.coord[0]
        for snake_length in self.coord[1:]:
            if x == snake_length[0] and y == snake_length[1]:
                return True

    def move(self, canvas):
        for x, y in self.coord:
            canvas.create_rectangle(x, y, x + SIZE_SPACE, y + SIZE_SPACE, fill=BODY_COLOR, outline=FIELD_COLOR)
        x, y = self.coord[0]

        if self.__direction == 'down':
            y += SIZE_SPACE
        elif self.__direction == 'up':
            y -= SIZE_SPACE
        elif self.__direction == 'left':
            x -= SIZE_SPACE
        elif self.__direction == 'right':
            x += SIZE_SPACE

        self.coord.insert(0, [x, y])
        head = canvas.create_rectangle(x, y, x + SIZE_SPACE, y + SIZE_SPACE, fill=HEAD_COLOR, outline=FIELD_COLOR)
        self.body_parts.insert(0, head)


