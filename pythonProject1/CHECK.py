import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)
character = gamebox.from_color(100,0,"black", 10, 10)
screen.fill()

direction_x = 1
direction_y = 1
speed = 5
game_on = False
walls = [
    gamebox.from_color(175, 250, "black", 350, 10),
    gamebox.from_color(625, 250, "black", 350, 10),
    gamebox.from_color(100, 450, "black", 200, 10),
    gamebox.from_color(575, 450, "black", 500, 10),
    gamebox.from_color(125, 625, "black", 500, 10),
    gamebox.from_color(650, 625, "black", 300, 10),
]  # start the game with three walls, notice walls (walls[0], walls[1]...) are not moved
counter = 0
random_blank = random.randint(0,800)
new_bar_left = gamebox.from_color((random_blank-15)/2, camera.y + 300, "black", (random_blank-15), 10)
new_bar_right = gamebox.from_color((800-(785-random_blank)/2), camera.y + 300, "black", 770-(random_blank-15), 10)

def tick(keys):
    global counter
    global direction_x
    global direction_y
    global speed
    global new_bar_left
    global new_bar_right
    global game_on


    if pygame.K_SPACE in keys:
        game_on = True

    if game_on == True:
        character.move_speed()
        character.yspeed = speed
        if pygame.K_RIGHT in keys:
            character.x += speed * direction_x
        if pygame.K_LEFT in keys:
            character.x -= speed * direction_x
        if character.x >= 800 or character.x <= 0 or character.y >= 600:
            speed = 0

        camera.y += 2

        counter += 1

        if counter % 50 == 0:  # controls the rate new walls are added
        # random x center, y window top,,random width, height

            walls.append(new_bar_left)
            walls.append(new_bar_right)

        if character.bottom_touches(new_bar_right):
            character.yspeed = 0
        if character.bottom_touches(new_bar_left):
            character.yspeed = 0

        for wall in walls:  # collision detection of character contact with each wall
            if character.touches(wall):
                character.move_to_stop_overlapping(wall)
            camera.draw(wall)

    camera.display()

ticks_per_second = 30
# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)