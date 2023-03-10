from tkinter import Tk, Label, Canvas

# https://www.youtube.com/watch?v=bfRwxS5d0SI
# from tkinter import ttk
import random


GAME_WIDTH = 700
GAME_HEIGHT = 700
BODY_PARTS = 6
START_SPEED = 400
SPACE_SIZE = 50
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BK_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food"
        )


def next_turn(snake, food):
    global direction
    x, y = snake.coordinates[0]

    if direction == "left" and next_direction != "right":
        direction = next_direction

    elif direction == "right" and next_direction != "left":
        direction = next_direction

    elif direction == "up" and next_direction != "down":
        direction = next_direction

    elif direction == "down" and next_direction != "up":
        direction = next_direction

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    sqaure = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
    )

    snake.squares.insert(0, sqaure)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global speed
        global score

        if speed > 50:
            speed -= 10

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        # this seems odd - why do you have to do this canvas.delete
        # you have to delete it on the canvas and in python - you have to manually keep them in sync
        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_col(snake):
        game_over()

    else:
        window.after(speed, next_turn, snake, food)


def change_dir(new_direction):
    global next_direction
    next_direction = new_direction


def check_col(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    canvas.delete("all")
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font="consolas, 70",
        text="GAME OVER",
        fill="red",
        tags="game_over",
    )


window = Tk()
window.title("Freds Snake Game")
window.resizable(False, False)

score = 0
direction = "down"
next_direction = "down"
speed = START_SPEED

label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=BK_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = 20
y = 20


window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_dir("left"))
window.bind("<Right>", lambda event: change_dir("right"))
window.bind("<Up>", lambda event: change_dir("up"))
window.bind("<Down>", lambda event: change_dir("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
