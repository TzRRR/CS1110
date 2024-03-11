# jumping puzzle game - pt1 - draw the score and timer on the screen
# Author unknown NOT Craig Dill, Mark Sherriff?  Luther Tychonievich?
import pygame
import gamebox
camera = gamebox.Camera(800, 600)

ticks = 9000
score = 0


def tick(keys):
    global ticks, score

    # clear display
    camera.clear("blue")

    # decrease ticks per call of tick()
    ticks -= 1

    # calculate ticks as seconds and lead fill with zero if necessary for three digits
    seconds = str(int((ticks/ticks_per_second))).zfill(3)

    # write timer and score to screen  Note: THESE gameboxes are created each tick
    #____________________________________________________________________________________________
    # NOTE: as of Spring 18 gamebox.from_text does not support the font argument
    # don't use time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, "arial", 24, "white")
    # current gamebox writes line above as:
    time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, 24, "white")
    # don't use score_box = gamebox.from_text(75, 30, "Score: " + str(score), "arial", 24, "white")
    # current gamebox writes line above as:
    score_box = gamebox.from_text(75, 30, "Score: " + str(score), 24, "white")
    #____________________________________________________________________________________________

    camera.draw(time_box)
    camera.draw(score_box)
    camera.display()


ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
