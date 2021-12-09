from pyglet import *
from pyglet.window import *
from math import *

from pyglet.window import mouse

if 'Variables' == 'Variables':
    cols = 7
    rows = 6
    col_width = row_height = 150
    grid_color = (255, 255, 255, 0)
    win_width = cols * col_width
    win_height = rows * row_height

window = Window(win_width, win_height)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print(f'THE MOUSE WAS CLICKED AT {x}, {y}, WHICH IS {column(x)}')


@window.event
def on_draw():
    window.clear
    draw_grid()
    draw_piece(200, 200, color=(255, 255, 255, 0))


def draw_grid():
    for i in range(cols):
        draw_line(i * row_height, 0, i * row_height, win_height, color=grid_color)
    for i in range(rows):
        draw_line(0, i * col_width, win_width, i * col_width, color=grid_color)


def draw_piece(x, y, color=(255, 255, 255, 0)):
    draw_reg_polygon(x, y, 50, 3, color)


def draw_reg_polygon(x, y, r, n, color=(255, 255, 255, 0)):
    vertices = []
    th = 0
    for _ in range(n):
        vertices += [x + r * sin(th), y + r * cos(th)]
        th += 2 * pi / n
        graphics.draw(n, gl.GL_POLYGON, ('v2f', vertices), ('c4B, color*n'))


def draw_line(x1, y1, x2, y2, color=(0, 255, 0, 0)):
    graphics.draw(2, gl.GL_LINES, ('v2i', (x1, y1, x2, y2)), ('c4B', color * 2))


def column(x):
    return x // col_width


app.run()
