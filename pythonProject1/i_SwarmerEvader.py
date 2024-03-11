"""
Craig Dill
Program implements swarmers and evaders
"""
import pygame
import gamebox
from random import randrange

WIDTH_WINDOW = 400
HEIGHT_WINDOW = 300
camera = gamebox.Camera(WIDTH_WINDOW, HEIGHT_WINDOW)  # size of window
character = gamebox.from_color(camera.x, camera.y, "blue", 10, 10)
swarmer = gamebox.from_color(randrange(WIDTH_WINDOW), randrange(HEIGHT_WINDOW), "red", 10, 10)
evader = gamebox.from_color(character.x + 15, character.y + 15, "green", 10, 10)
speed = 2
direction_x = 1
direction_y = 1


def tick(keys):
    global direction_x
    global direction_y
    global speed

    if pygame.K_RIGHT in keys:
        character.x += speed * direction_x
    if pygame.K_LEFT in keys:
        character.x -= speed * direction_x
    if pygame.K_UP in keys:
        character.y -= speed * direction_y
    if pygame.K_DOWN in keys:
        character.y += speed * direction_y

    # update the swarmer position
    if character.x < swarmer.x:
        swarmer.x -= 1
    elif character.x > swarmer.x:
        swarmer.x += 1

    if character.y < swarmer.y:
        swarmer.y -= 1
    elif character.y > swarmer.y:
        swarmer.y += 1

    # update evader position
    if character.x < evader.x:
        evader.x += 1
    elif character.x > evader.x:
        evader.x -= 1
    if character.y < evader.y:
        evader.y += 1
    elif character.y > evader.y:
        evader.y -= 1

    camera.clear("black")
    camera.draw(evader)
    camera.draw(character)
    camera.draw(swarmer)
    camera.display()

TICKS_PER_SECOND = 10

gamebox.timer_loop(TICKS_PER_SECOND, tick)
