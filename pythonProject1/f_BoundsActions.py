# Craig Dill (cd9au)
# Determine if a gamebox is exiting the player window and if so apply a bounds action
import pygame
import gamebox

WIDTH_WINDOW = 400
HEIGHT_WINDOW = 300
camera = gamebox.Camera(WIDTH_WINDOW, HEIGHT_WINDOW)  # size of window
character = gamebox.from_color(camera.x, camera.y, "green", 10, 10)
speed = 2                                         # higher number, faster gamebox moves
# Enable only one of the following four BOUNDS_ACTIONs
BOUNDS_ACTION = "wrap"                            # If set to wrap exit one side, enter opposite side
# BOUNDS_ACTION = "bounce"                         # if set to bounce then deflect like ball
# BOUNDS_ACTION = "stop"                          # if stop, hold position on screen edge
# BOUNDS_ACTION = "remove"                        # if set to remove keep off the screen

direction_x = 1                                   # flip flops between 1 & -1 determining direction
direction_y = 1


def tick(keys):
    global direction_x
    global direction_y
    global speed
    # Use pygame key definitions to detect user keyboard input.  Parameter keys can
    # have more than one key.
    # if the decision statements below are converted into if elif, only one key is
    # detected each tick, even though multiple keys are pressed
    if pygame.K_RIGHT in keys:
        character.x += speed * direction_x  # add constant value to .x moves at constant speed
    if pygame.K_LEFT in keys:
        character.x -= speed * direction_x  # same for subtract
    if pygame.K_UP in keys:
        character.y -= speed * direction_y  # same for y
    if pygame.K_DOWN in keys:
        character.y += speed * direction_y

    if BOUNDS_ACTION == "wrap":
        # Determine bounds contact and if so, wrap
        if character.x >= WIDTH_WINDOW:
            character.x = 0                     # wrap
        elif character.x <= 0:
            character.x = WIDTH_WINDOW
        elif character.y <= 0:
            character.y = HEIGHT_WINDOW
        elif character.y >= HEIGHT_WINDOW:
            character.y = 0

    elif BOUNDS_ACTION == "bounce":
        # Determine bounds contact and if so, bounce
        if character.x >= WIDTH_WINDOW or character.x <= 0:
            direction_x *= -1  # create the bounce by flipping x direction

        if character.y >= HEIGHT_WINDOW or character.y <= 0:
            direction_y *= -1  # create the bounce by flipping y direction
            
    elif BOUNDS_ACTION == "stop":
        # Determine bounds contact and if so freeze character
        if character.x >= WIDTH_WINDOW or character.x <= 0 or character.y >= HEIGHT_WINDOW \
                or character.y <= 0:
            speed = 0   # freeze character by stopping all motion
    
    elif BOUNDS_ACTION == "remove":
        # Determine bounds contact and if so, move character off screen
        if character.x >= WIDTH_WINDOW or character.x <= 0 or character.y >= HEIGHT_WINDOW \
                or character.y <= 0:
            character.left = WIDTH_WINDOW + 1

    camera.clear("red")
    camera.draw(character)
    camera.display()


TICKS_PER_SECOND = 30

# keep this line the last one in your program
gamebox.timer_loop(TICKS_PER_SECOND, tick)
