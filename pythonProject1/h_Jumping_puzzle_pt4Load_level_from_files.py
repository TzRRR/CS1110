# jumping puzzle game - pt4 - load a level from a file

# level.csv  must be in same folder as this program
# ground,-100,600,3000,100
# platform,200,500,100,15
# platform,400,500,100,15
# coin,150,450
# coin,250,450

import pygame
import gamebox
camera = gamebox.Camera(800,600)

character = gamebox.from_color(50, 50, "red", 15, 40)
character.yspeed = 0
walls = []
coins = []
ticks = 9000
score = 0

def load_level(level_name):                         # new
    level_file = open(level_name, "r")

    for line in level_file:
        split = line.strip().split(",")
        if split[0] == "ground" or split[0] == "platform":
            walls.append(gamebox.from_color(int(split[1]), int(split[2]), "black", int(split[3]), int(split[4])))
        elif split[0] == "coin":
            coins.append(gamebox.from_color(int(split[1]), int(split[2]), "yellow", 12, 12))


def tick(keys):
    global ticks, score

    # clear display
    camera.clear("blue")

    # decrease timer per call of tick
    ticks -= 1

    # calculate timer
    seconds = str(int((ticks/ticks_per_second))).zfill(3)

    if pygame.K_RIGHT in keys:
        character.x += 5
    if pygame.K_LEFT in keys:
        character.x -= 5
    character.yspeed += 1
    character.y = character.y + character.yspeed

    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -15
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)

    for coin in coins:
        if character.touches(coin):
            score += 1
            coins.remove(coin)
        camera.draw(coin)

    # write timer and score to screen  Note: THESE gameboxes are created each tick
    #____________________________________________________________________________________________
    # NOTE: as of Spring 18 gamebox.from_text does not support the font argument
    # time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, "arial", 24, "white")
    # current gamebox writes line above as:
    time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, 24, "white")
    # score_box = gamebox.from_text(75, 30, "Score: " + str(score), "arial", 24, "white")
    # current gamebox writes line above as:
    score_box = gamebox.from_text(75, 30, "Score: " + str(score), 24, "white")
    #____________________________________________________________________________________________

    camera.draw(time_box)
    camera.draw(score_box)

    # draw the character
    camera.draw(character)

    # display the screen
    camera.display()


ticks_per_second = 30

load_level("level.csv")

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
