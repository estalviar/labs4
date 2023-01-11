from tkinter import *
from config import *
from Snake import Snake
from Food import Food


def check_exit_field():
    x, y = snake.coord[0]
    if x < 0 or x >= WIDTH_WINDOW:
        return True
    elif y < 0 or y >= HEIGHT_WINDOW:
        return True


def start_game(food):
    x, y = snake.coord[-1]
    if food.is_eating(x, y):
        canvas.delete(food)
        food = Food()
        food.create_food(canvas)
    else:
        canvas.create_rectangle(x, y, x + SIZE_SPACE, y + SIZE_SPACE, fill=FIELD_COLOR, outline=FIELD_COLOR)
        del snake.coord[-1]
        canvas.delete(snake.body_parts[-1])
        del snake.body_parts[-1]

    if snake.check_snake_crash() or check_exit_field():
        end_game(len(snake.coord))
    else:
        snake.move(canvas)
        window.after(SPEED_SNAKE, start_game, food)


def end_game(score):
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('Calibri', 40), text='Game Over! ' + f'Счёт: {score + 1}.',
                       fill=FOOD_COLOR)


window = Tk()
window.title('Игра "Змейка"')
window.resizable(False, False)
window.geometry(f'{WIDTH_WINDOW}x{HEIGHT_WINDOW}')

canvas = Canvas(window, height=HEIGHT_WINDOW, width=WIDTH_WINDOW, bg=FIELD_COLOR)
canvas.pack()

food = Food()
food.create_food(canvas)

snake = Snake()
snake.create_snake(canvas)

window.bind('<Down>', lambda event: snake.set_direction('down'))
window.bind('<Up>', lambda event: snake.set_direction('up'))
window.bind('<Left>', lambda event: snake.set_direction('left'))
window.bind('<Right>', lambda event: snake.set_direction('right'))

snake.move(canvas)
start_game(food)
window.mainloop()
