# Tianze Ren tr2bx
import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
character = gamebox.from_color(50, 0, "red", 30, 30)
ticks = 0
walls = [
    gamebox.from_color(175, 250, "black", 370, 10),
    gamebox.from_color(625, 250, "black", 370, 10),
    gamebox.from_color(100, 450, "black", 220, 10),
    gamebox.from_color(575, 450, "black", 520, 10),
    gamebox.from_color(125, 625, "black", 520, 10),
    gamebox.from_color(650, 625, "black", 320, 10),
]
counter = 0



def tick(keys):
    global counter, ticks
    counter += 1
    if pygame.K_RIGHT in keys:
        character.x += 10
    if pygame.K_LEFT in keys:
        character.x -= 10
    if character.y >= 585 + 2 * counter:
        character.yspeed = 0
    if character.x >= 800:
        character.x = 800
    if character.x <= 0:
        character.x = 0
    character.yspeed += 1
    character.y = character.y + character.yspeed

    camera.clear("white")
    camera.draw(character)
    camera.y += 2

    if counter % 70 == 0:
        random_blank = random.randint(0,800)
        new_bar_left = gamebox.from_color((random_blank-30)/2, camera.y + 300, "black", (random_blank-30), 10)
        new_bar_right = gamebox.from_color((800-(770-random_blank)/2), camera.y + 300, "black", 740-(random_blank-30), 10)
        walls.append(new_bar_left)
        walls.append(new_bar_right)

    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)


    ticks += 1
    seconds = str(int((ticks/ticks_per_second)))
    time_box = gamebox.from_text(100, 550 + 2 * counter, "Time: " + seconds, 24, "red")
    camera.draw(time_box)

    if character.y < 2 * counter - 16:
        info = gamebox.from_text(400, 300 + 2 * counter, "Game Over", 80, "red")
        gamebox.pause()
        camera.draw(info)

    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
