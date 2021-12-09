from pyglet import *
from pyglet.window import *

window = Window(1000, 1000)


@window.event
def on_draw():
    window.clear()
    player_sprite.draw()


def update(dt):
    player_sprite.x += plyr_dx * dt
    player_sprite.y += plyr_dy * dt


@window.event
def on_key_press(symbol, modifiers):
    global plyr_dx, plyr_dy
    if symbol == key.LEFT:
        plyr_dx = -plyr_speed
        plyr_dy = 0
    elif symbol == key.RIGHT:
        plyr_dx = +plyr_speed
        plyr_dy = 0
    elif symbol == key.UP:
        plyr_dy = +plyr_speed
        plyr_dx = 0
    elif symbol == key.DOWN:
        plyr_dy = -plyr_speed
        plyr_dx = 0


resource.path = ['resources']
resource.reindex()

player_img = resource.image('player.png')

player_sprite = sprite.Sprite(img=player_img, x=500, y=500)

plyr_speed = 500
plyr_dx = 0
plyr_dy = 0

clock.schedule_interval(update, 1 / 120)

app.run()
