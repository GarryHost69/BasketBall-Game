import pygame
import random
import math


pygame.init()
max_velocity = 50
low_velocity = 10
avg_velocity = 25
width = 1200
height = 600
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
logo = pygame.image.load('Basketball.png')
ball = pygame.transform.scale(pygame.image.load('Basketball.png'), (100, 100))
hoop = pygame.transform.scale(pygame.image.load('Hoop.png'), (100, 100))
pygame.display.set_icon(logo)
pygame.display.set_caption('BasketBall')
screen = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()


def getInitialVelocity(lv):
    i = random.randint(0, 1)
    if lv > 450 and lv < 490:
        if i == 0:
            vel = max_velocity + 1.5
        else:
            vel = max_velocity - 1.5
    elif lv > 490 and lv < 510:
        if i == 0:
            vel = avg_velocity + 1.5
        else:
            vel = avg_velocity - 1.5
    else:
        if i == 0:
            vel = low_velocity + 1.5
        else:
            vel = low_velocity - 1.5
    return vel


def xDisp(u, t, theta):
    return u * t * math.cos(theta)


def yDisp(u, t, theta):
    return (u * t * math.sin(theta)) - (0.5 * 9.8 * math.pow(t, 2))


def drawLever(lev_x, lev_y):
    pygame.draw.line(screen, black, (lev_x + 10, lev_y), (lev_x + 30, lev_y), 3)


def drawPowerBar():
    pygame.draw.rect(screen, red, [1100, 450, 20, 40])
    pygame.draw.rect(screen, green, [1100, 490, 20, 20])
    pygame.draw.rect(screen, yellow, [1100, 510, 20, 40])


def displayHoop(x, y):
    screen.blit(hoop, (x, y))


def displayBasketBall(bx, by):
    screen.blit(ball, (bx, by))


if __name__ == '__main__':
    lev_x = 1090
    lev_y = 480
    lev_col = False
    collision = False
    lever_lock = False
    x = 350
    y = 350
    running = True
    while running:
        if y > height - 90:
            collision = True
            pygame.mixer.music.load('BOUNCE.mp3')
            pygame.mixer.music.play()
        if y < 250:
            collision = False
            pygame.mixer.music.play()
        if lev_y > 550:
            lev_col = True
        if lev_y < 450:
            lev_col = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    lever_lock = True
                elif event.key == pygame.K_a and not lever_lock:
                    x -= 20
                    y += 20
                elif event.key == pygame.K_d and not lever_lock:
                    x += 20
                    y += 20
        screen.fill(white)
        displayHoop(width/2 - 50, 100)
        displayBasketBall(x, y)
        drawPowerBar()
        drawLever(lev_x, lev_y)
        clock.tick(60)
        pygame.display.update()
        if collision:
            y -= 5
        else:
            y += 5
        if not lever_lock:
            if lev_col:
                lev_y -= 3
            else:
                lev_y += 3
        else:
            u = getInitialVelocity(lev_y)
            angle = 60
            t = 0
            cntr = True
            while cntr:
                dx = xDisp(u, t, angle)
                dy = yDisp(u, t, angle)
                if x - dx < 0:
                    cntr = False
                if y + dy < 0:
                    cntr = False
                if x - dx > width:
                    cntr = False
                if y + dy > width:
                    cntr = False

                if cntr:
                    x -= dx
                    y += dy
                t += 0.5
                print(x, y)
                screen.fill(white)
                displayHoop(width / 2 - 50, 100)
                displayBasketBall(x, y)
                drawPowerBar()
                drawLever(lev_x, lev_y)
                clock.tick(15)
                pygame.display.update()

            input('GetCh() : ')
            running = False

