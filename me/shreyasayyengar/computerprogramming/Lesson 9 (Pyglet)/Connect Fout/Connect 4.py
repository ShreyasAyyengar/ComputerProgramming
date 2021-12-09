from pyglet import app
from pyglet import clock
from pyglet.window import Window
from pyglet.window import mouse
from pyglet.window import key
from pyglet import graphics
from pyglet import gl
from pyglet import text
from math import sin, cos, pi

cols = 7  # don't change this
rows = 6  # don't change this
col_width = row_height = 100  # change if you like
grid_color = (255, 0, 0, 0)  # change color if you like
piece_radius = row_height * 0.4  # change if you like, from 0.1 to 0.5
p1_color = (255, 0, 0, 0)
p2_color = (0, 0, 255, 0)

win_width = cols * col_width
win_height = rows * row_height

window = Window(win_width, win_height)


@window.event
def on_mouse_press(x, y, button, modifiers):
    global last_col_clicked
    if button == mouse.LEFT and last_col_clicked == -1:
        last_col_clicked = column(x)
    # print(f'The mouse button was clicked at {x}, {y}, which is in column {column(x)}.' )


def update(dt):
    global last_col_clicked, player, game_over
    if game_over:
        return
    if last_col_clicked != -1:
        if pieces_per_column[last_col_clicked] < rows:
            print(f'Player {player} placed a piece in column {last_col_clicked}.')
            grid[pieces_per_column[last_col_clicked]][last_col_clicked] = player
            pieces_per_column[last_col_clicked] += 1
            winning_line = get_winning_line()
            if len(winning_line) == 4:
                game_over = True
                print(f'Winning line is: {winning_line}')
                print(f'Player {player} has won.')
            player = 2 if player == 1 else 1
            # print(grid)
            # print(pieces_per_column)
        last_col_clicked = -1


@window.event
def on_draw():
    window.clear()
    draw_grid()
    draw_all_pieces()


def draw_all_pieces():
    for y, row in enumerate(grid):
        for x, player_piece in enumerate(row):
            if player_piece == 1:
                draw_piece(x, y, p1_color)
            elif player_piece == 2:
                draw_piece(x, y, p2_color)


def draw_grid():
    for i in range(cols):
        draw_line(i * row_height, 0, i * row_height, win_height, color=grid_color)
    for i in range(rows):
        draw_line(0, i * col_width, win_width, i * col_width, color=grid_color)


def draw_piece(x, y, color=(255, 255, 255, 0)):
    draw_reg_polygon(x * col_width + col_width // 2, y * row_height + row_height // 2, piece_radius, 64, color)


def draw_reg_polygon(x, y, r, n, color=(255, 255, 255, 0)):
    vertices = []
    th = 0
    for _ in range(n):
        vertices += [x + r * sin(th), y + r * cos(th)]
        th += 2 * pi / n
    graphics.draw(n, gl.GL_POLYGON, ('v2f', vertices), ('c4B', color * n))


def draw_line(x1, y1, x2, y2, color=(255, 255, 255, 0)):
    graphics.draw(2, gl.GL_LINES, ('v2i', (x1, y1, x2, y2)), ('c4B', color * 2))


def get_winning_line():
    for row in range(0, rows):  # for horizontal line win
        for col in range(0, 4):  # start with leftmost columns
            if all([grid[row][col] == value and value != 0 for value in grid[row][col:col + 4]]):
                return (col, row), (col + 1, row), (col + 2, row), (col + 3, row)
    transpose = list(zip(*grid))
    for col in range(0, cols):  # for vertical line win
        for row in range(0, 3):  # start with bottom on up
            if all([transpose[col][row] == value and value != 0 for value in transpose[col][row:row + 4]]):
                return (col, row), (col, row + 1), (col, row + 2), (col, row + 3)
    for row in range(3, rows):  # for diagonals DOWN and to RIGHT, start w upper rows
        for col in range(0, 4):  # start with leftmost columns
            if (grid[row][col] != 0
                    and grid[row][col] == grid[row - 1][col + 1]
                    and grid[row][col] == grid[row - 2][col + 2]
                    and grid[row][col] == grid[row - 3][col + 3]):
                return (col + 3, row - 3), (col + 2, row - 2), (col + 1, row - 1), (col, row)
    for row in range(3, rows):  # for diagonals DOWN and to LEFT, start w upper rows.
        for col in range(3, cols):  # start with rightmost columns
            if (grid[row][col] != 0
                    and grid[row][col] == grid[row - 1][col - 1]
                    and grid[row][col] == grid[row - 2][col - 2]
                    and grid[row][col] == grid[row - 3][col - 3]):
                return (col - 3, row - 3), (col - 2, row - 2), (col - 1, row - 1), (col, row)
    return ()  # if no winning line, return an empty tuple


def column(x):
    return x // col_width


grid = [[0] * cols for i in range(rows)]
pieces_per_column = [0] * cols

last_col_clicked = -1  # this will change, -1 means no column clicked yet
player = 1  # this toggles between 1 and 2
game_over = False

clock.schedule_interval(update, 1 / 15)

app.run()