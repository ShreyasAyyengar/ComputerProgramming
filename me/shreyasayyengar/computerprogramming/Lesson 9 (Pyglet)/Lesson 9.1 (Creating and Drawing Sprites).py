from pyglet import *
from pyglet.window import *
from pyglet import graphics
from random import *

import sys

window = Window(1000, 1000)


@window.event
def on_draw():
    global snk_x, snk_y
    if not gameOver:
        window.clear()
        draw_square(snk_x, snk_y, snk_size)
        draw_square(f_x, f_y, snk_size, color=(255, 0, 255, 0))


def draw_square(x, y, size, color=(255, 0, 255, 0)):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x, y)


def place_food():
    global f_x, f_y
    f_x = randint(0, (window.width // snk_size) - 1) * snk_size
    f_y = randint(0, (window.height // snk_size) - 1) * snk_size


@window.event
def on_key_press(symbol, modifiers):
    global snk_dx, snk_dy, app
    if symbol == key.LEFT:
        snk_dx = -snk_size
        snk_dy = 0
    elif symbol == key.RIGHT:
        snk_dx = snk_size
        snk_dy = 0
    elif symbol == key.UP:
        snk_dx = 0
        snk_dy = snk_size
    elif symbol == key.DOWN:
        snk_dx = 0
        snk_dy = -snk_size


def update(dt):
    global snk_x, snk_y, snk_dx, snk_dy, snk_size, app, gameOver, window, score
    if snk_x < 0 or snk_x + snk_dx == window.width or snk_y == 0 or snk_y + snk_dy == window.height:  # checks to prevent sprint from going off screen
        gameOver = True
        app.exit()
        window.close
    snk_x += snk_dx
    snk_y += snk_dy
    if snk_x == f_x and snk_y == f_y:
        place_food()
        print("DEBUGGING : place_food was called sucessfully")
        score += 1
        print(f'Your score is {score}')


snk_size = 25  # Width and Height of Snake

snk_dx, snk_dy = 0, 0

f_x, f_y = 0, 0
score = 0

snk_x = window.width // snk_size // 2 * snk_size
snk_y = window.height // snk_size // 2 * snk_size

place_food()

gameOver = False

if gameOver == True:
    window.close()

clock.schedule_interval(update, 1 / 10)  # Essentially the sprite speed(but objected as ref«resh interval

app.run()
