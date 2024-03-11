# jumping puzzle game - pt2 - add moving character and walls (ground/platform)

import pygame
import gamebox
camera = gamebox.Camera(800,600)

character = gamebox.from_color(50, 50, "red", 15, 40)       # new
character.yspeed = 0

walls = [gamebox.from_color(-100, 600, "black", 3000, 100),
         gamebox.from_color(450,500,"black",200,10)]        # new
ticks = 9000
score = 0


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

    character.yspeed += 1                           # accelerate character
    character.y = character.y + character.yspeed    # from current y location

    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -15
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)


    # write timer and score to screen  Note: THESE gameboxes are created each tick
    #____________________________________________________________________________________________
    # NOTE: as of Spring 18 gamebox.from_text does not support the font argument
    # don't use. time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, "arial", 24, "white")
    # current gamebox writes line above as:
    time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, 24, "white")
    # don't use score_box = gamebox.from_text(75, 30, "Score: " + str(score), "arial", 24, "white")
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

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
