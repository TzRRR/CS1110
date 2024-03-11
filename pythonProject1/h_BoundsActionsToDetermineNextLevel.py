"""
Craig Dill (cd9au)
If player exits window edge right, load new background to represent
next level of play.  Here the background is simply a new clear color,
however an image sized the same as the camera view attached to a
gamebox (using gamebox from image) and drawn first each tick, works
the same, providing more interesting backgrounds.
"""
import pygame
import gamebox

WIDTH_WINDOW = 400
HEIGHT_WINDOW = 300
camera = gamebox.Camera(WIDTH_WINDOW, HEIGHT_WINDOW)  # size of window
character = gamebox.from_color(camera.x, camera.y, "green", 10, 10)
speed = 2                        # higher number, faster gamebox moves
# Enable only one of the following four BOUNDS_ACTIONs
BOUNDS_ACTION = "wrap"
# BOUNDS_ACTION = "bounce"
# BOUNDS_ACTION = "stop"
# BOUNDS_ACTION = "remove"

direction_x = 1
direction_y = 1
background_colors = ["red", "yellow", "blue"]  # new for NextLevel
background_colors_count = 0                    # new for NextLevel


def tick(keys):
    global direction_x
    global direction_y
    global speed
    global background_colors_count             # new for NextLevel

    if pygame.K_RIGHT in keys:
        character.x += speed * direction_x
    if pygame.K_LEFT in keys:
        character.x -= speed * direction_x
    if pygame.K_UP in keys:
        character.y -= speed * direction_y
    if pygame.K_DOWN in keys:
        character.y += speed * direction_y

    if BOUNDS_ACTION == "wrap":
        if character.x >= WIDTH_WINDOW:
            character.x = 0
            background_colors_count += 1      # new for NextLevel
            if background_colors_count == len(background_colors):  # new
                background_colors_count = 0   # new
        elif character.x <= 0:
            character.x = WIDTH_WINDOW
        elif character.y <= 0:
            character.y = HEIGHT_WINDOW
        elif character.y >= HEIGHT_WINDOW:
            character.y = 0

    elif BOUNDS_ACTION == "bounce":
        if character.x >= WIDTH_WINDOW or character.x <= 0:
            direction_x *= -1
        if character.y >= HEIGHT_WINDOW or character.y <= 0:
            direction_y *= -1
    elif BOUNDS_ACTION == "stop":
        if character.x >= WIDTH_WINDOW or character.x <= 0 or character.y >= HEIGHT_WINDOW \
                or character.y <= 0:
            speed = 0
    elif BOUNDS_ACTION == "remove":
        if character.x >= WIDTH_WINDOW or character.x <= 0 or character.y >= HEIGHT_WINDOW \
                or character.y <= 0:
            character.left = WIDTH_WINDOW + 1

    camera.clear(background_colors[background_colors_count])
    camera.draw(character)
    camera.display()

TICKS_PER_SECOND = 30

# keep this line the last one in your program
gamebox.timer_loop(TICKS_PER_SECOND, tick)
