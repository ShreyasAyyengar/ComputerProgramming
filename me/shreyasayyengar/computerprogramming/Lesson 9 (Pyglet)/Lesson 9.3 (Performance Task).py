from pyglet import *
from pyglet.window import *
from random import *
from random import *

window = Window(1000, 200)
# THIS CODE DECIDES THE THE WIDTH AND HEIGHT
# OF THE CANVAS, SINCE IT SHOULD NOT BE A
# PERFECT SQUARE, THEY SHOULD BE IRRATIONAL


@window.event # LISTENS TO THE WINDOW OPEN EVENT
def on_draw():
    global sqr_x, sqr_y
    if not gameOver:
        window.clear()
        draw_square(sqr_x, sqr_y, sqr_size, color=(102, 255, 255, 0))
        draw_square(f_x, f_y, 45, color=(255, 255, 153, 0))

# THIS SERVES AS THE BASE METHOD FOR DRAWING ANYTHING
# FROM SQUARES TO CIRCLES, TO ASSORTED SPRITES


def draw_square(x, y, size, color=(255, 0, 255, 0)):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x, y)

    # THIS FUNCTION ACTUALLY PLACES THE SQUARE TAKING IN 4
    # PARAMETRES ==> X, Y, SIZE, COLOR=(HEX CODE)


def place_other_food():
    global f_x, f_y
    f_x = randint(0, (window.width // sqr_size) - 1) * sqr_size
    f_y = randint(0, (window.height // sqr_size) - 1) * sqr_size

    # THIS METHOD PLACES THE OTHER SQUARE THAT MOVES DYNAMICALLY!
    # BECAUSE THIS IS A DYNAMIC SPRITE, IT NEEDS TO BE CALLED IN
    # UPDATE FUNCTION BELOW


# def draw_game_over():
#     gameOverScreen = text.Label(f'Your Score is {score}', font_size=28, x=window.width // 2, y=window.height // 2,
#                                 anchor_x='center', anchor_y='center')
#     gameOverScreen.draw()


@window.event
def on_key_press(symbol, modifiers): # THIS SECTION OF
    global sqr_dx, sqr_dy, app       # CODE IS MADE TO CONTROL THE
    if symbol == key.LEFT:           # SPRITES, LEFT, RIGHT, UP, DOWN
        if sqr_dx == 0:
            sqr_dx = -sqr_size
            sqr_dy = 0
    elif symbol == key.RIGHT:
        if sqr_dx == 0:
            sqr_dx = sqr_size
            sqr_dy = 0
    elif symbol == key.UP:
        if sqr_dy == 0:
            sqr_dx = 0
            sqr_dy = sqr_size
    elif symbol == key.DOWN:
        if sqr_dy == 0:
            sqr_dx = 0
            sqr_dy = -sqr_size


def update(dt):
    global sqr_x, sqr_y, sqr_dx, sqr_dy, sqr_size, app, gameOver, window, score
    if sqr_x < 0 or sqr_x + sqr_dx == window.width or sqr_y == 0 or sqr_y + sqr_dy == window.height:  # checks to prevent sprite from going off screen
        gameOver = True
        app.exit
        window.clear()
        window.close
        # draw_game_over()

        return

    if (sqr_x, sqr_y) in tail:
        gameOver = True
        window.clear
        # draw_game_over()
        return

    tail.append((sqr_x, sqr_y))

    sqr_x += sqr_dx
    sqr_y += sqr_dy
    if sqr_x == f_x and sqr_y == f_y:
        gameOver = True
        print("DEBUGGING : place_other_food() was called sucessfully")
        score += 1
        print(f'Your score is {score}')
    else:
        tail.pop(0)

    print(tail)


sqr_size = 25  # Width and Height of Snake

sqr_dx, sqr_dy = 0, 0

f_x, f_y = 0, 0
score = 0

sqr_x = window.width // sqr_size // 2 * sqr_size
sqr_y = window.height // sqr_size // 2 * sqr_size

place_other_food()

gameOver = False

if gameOver == True:
    app.exit
    window.close()

tail = []

clock.schedule_interval(update, 1 / 12)  # Essentially the sprite speed(but objected as ref«resh interval

app.run()
