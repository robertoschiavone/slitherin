import random
import tkinter as tk

import pygame

from tkinter import messagebox

from Cube import Cube
from Snake import Snake


def draw_grid(width, rows, surface):
    size_between = width // rows

    x = 0
    y = 0
    for i in range(rows):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def redraw_window(surface, snake, snack):
    global rows, width
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:
            continue
        else:
            break

    return x, y


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


if __name__ == "__main__":
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube(random_snack(rows, snake), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].position == snack.position:
            snake.add_cube()
            snack = Cube(random_snack(rows, snake), color=(0, 255, 0))

        for x in range(len(snake.body)):
            if snake.body[x].position in list(map(lambda z: z.position,
                                                  snake.body[x + 1:])):
                print(f"Score: {len(snake.body)}")
                message_box("You lost!", "Play again...")
                snake.reset((10, 10))
                break

        redraw_window(win, snake, snack)
