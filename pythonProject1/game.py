# Tianze Ren tr2bx
"""
This game is about controlling the spaceship to survive in the outer space. The player would
press the left and right key on the keyboard to control the movement of the spaceship.
When the spaceship moves out of the left and right boundary, it appears back at the opposite side
of the screen. There would be coins (collectibles) ahead for the spaceship to collect. When the
number of coins is equal or greater then 4, the player has a chance not to die when having contact
with the bombs. There would be bombs (enemies) ahead that the spaceship needs to avoid. Everytime
the spaceship has a contact with a bomb, the speed of the spaceship increases. When the game ends,
the player can press r to restart the game.
"""
import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
character = gamebox.from_image(400, 550, "plane.png")

counter = 0
score = 0
ticks = 0
frequency = 20
obstacles = []
stars = []
coins = [gamebox.from_color(100, 344, "yellow", 10, 10)]

dead = False

def tick(keys):
    """
    This function detects keyboard presses, gamebox creation, movement, and collision, and camera movement in every tick
    :param keys: keyboard presses
    :return: no return
    """
    global counter, score, ticks, dead, stars, obstacles, coins, character, frequency
    if not dead:
        if pygame.K_RIGHT in keys:
            character.x += 10
        if pygame.K_LEFT in keys:
            character.x -= 10

        if character.left >= 800:
            character.right = 1
        elif character.right <= 0:
            character.left = 800 - 1

        camera.clear("black")
        camera.draw(character)
        camera.y -= 12
        counter += 1
        character.y -= 12

        if counter % 3 == 0:
            numstars = random.randint(0, 7)
            for i in range(numstars):
                stars.append(gamebox.from_color(random.randint(5, 800 - 5), 0, "white", 3, 3))
        for star in stars:
            star.y -= 12
            if star.y > 600:
                stars.remove(star)
            camera.draw(star)

        if counter % frequency == 0:
            enemies = gamebox.from_image(random.randint(0,800), camera.y - 300, "bomb.png")
            obstacles.append(enemies)


        if counter % 70 == 0:
            coin = gamebox.from_color(random.randint(10, 790), camera.y - 300, "yellow", 12, 12)

            coins.append(coin)

        for coin in coins:
            if character.touches(coin):
                score += 1
                coins.remove(coin)
            camera.draw(coin)

        for obstacle in obstacles:
            if character.touches(obstacle) and score < 4:
                info = gamebox.from_text(400, camera.y, "Game Over", 80, "red")
                restart = gamebox.from_text(400, camera.y + 100, "Press r to restart", 50, "red")
                camera.draw(info)
                camera.draw(restart)
                dead = True
            elif character.touches(obstacle) and score >= 4:
                obstacles.remove(obstacle)
                score -= 4
                frequency -= 4

            camera.draw(obstacle)

        ticks += 1
        seconds = str(int((ticks / ticks_per_second)))
        time_box = gamebox.from_text(100, 50 - 12 * counter, "Time: " + seconds, 24, "red")
        camera.draw(time_box)

        energy = gamebox.from_text(700, 50 - 12 * counter, "Number of Coins: " + str(score), 24, "red")
        camera.draw(energy)


        camera.display()

    else:
        if pygame.K_r in keys:
            dead = False
            camera.x = 400
            camera.y = 300
            character = gamebox.from_image(400, 550, "plane.png")

            counter = 0
            score = 0
            ticks = 0
            frequency=20
            obstacles = []
            stars = []
            coins = [gamebox.from_color(100, 344, "yellow", 10, 10)]


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)