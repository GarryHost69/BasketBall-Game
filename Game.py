import pygame
import random
import math


pygame.init()
max_velocity = 50
low_velocity = 10
avg_velocity = 25
width = 1200
height = 600
grey = (192, 192, 192)
white = (255, 255, 255)
black = (0, 0, 0)
char = ''
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
logo = pygame.image.load('Img/Basketball.png')
ball = pygame.transform.scale(pygame.image.load('Img/Basketball.png'), (100, 100))
hoop = pygame.transform.scale(pygame.image.load('Img/Hoop.png'), (100, 100))
In1 = pygame.transform.scale(pygame.image.load('Img/MainM1.png'), (width, height))
In2 = pygame.transform.scale(pygame.image.load('Img/MainM2.jpg'), (width, height))
In3 = pygame.transform.scale(pygame.image.load('Img/MainM3.jpg'), (width, height))
In4 = pygame.transform.scale(pygame.image.load('Img/MainM4.png'), (width, height))
In5 = pygame.transform.scale(pygame.image.load('Img/MainM5.jpg'), (width, height))
Akashi = pygame.transform.scale(pygame.image.load('Img/Akashi.png'), (150, 200))
Aomine = pygame.transform.scale(pygame.image.load('Img/Aomine.jpg'), (150, 200))
Kagami = pygame.transform.scale(pygame.image.load('Img/Kagami.png'), (150, 200))
Kise = pygame.transform.scale(pygame.image.load('Img/Kise.jpg'), (150, 200))
Kuroko = pygame.transform.scale(pygame.image.load('Img/Kuroko.png'), (150, 200))
Murasakibara = pygame.transform.scale(pygame.image.load('Img/Murasakibara.png'), (150, 200))
Midorima = pygame.transform.scale(pygame.image.load('Img/Midorima.jpg'), (150, 200))
InArr = [In1, In2, In3, In4, In5]
pygame.display.set_icon(logo)
pygame.display.set_caption('BasketBall')
screen = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()


def displayCharacters():
    txt = pygame.font.Font('freesansbold.ttf', 30)
    textsurf = text_objects('Select Your Character', txt)
    screen.blit(textsurf, (400, 0))
    pygame.draw.rect(screen, black, (170, 45, 160, 210))
    pygame.draw.rect(screen, black, (370, 45, 160, 210))
    pygame.draw.rect(screen, black, (570, 45, 160, 210))
    pygame.draw.rect(screen, black, (770, 45, 160, 210))
    pygame.draw.rect(screen, black, (295, 315, 160, 210))
    pygame.draw.rect(screen, black, (495, 315, 160, 210))
    pygame.draw.rect(screen, black, (695, 315, 160, 210))
    txt = pygame.font.Font('freesansbold.ttf', 20)
    screen.blit(Akashi, (175, 50))
    textsurf = text_objects('Akashi', txt)
    screen.blit(textsurf, (220, 260))
    screen.blit(Aomine, (375, 50))
    textsurf = text_objects('Aomine', txt)
    screen.blit(textsurf, (420, 260))
    screen.blit(Kagami, (575, 50))
    textsurf = text_objects('Kagami', txt)
    screen.blit(textsurf, (620, 260))
    screen.blit(Kise, (775, 50))
    textsurf = text_objects('Kise', txt)
    screen.blit(textsurf, (820, 260))
    screen.blit(Kuroko, (300, 320))
    textsurf = text_objects('Kuroko', txt)
    screen.blit(textsurf, (345, 530))
    screen.blit(Murasakibara, (500, 320))
    textsurf = text_objects('Murasakibara', txt)
    screen.blit(textsurf, (515, 530))
    screen.blit(Midorima, (700, 320))
    textsurf = text_objects('Midorima', txt)
    screen.blit(textsurf, (735, 530))


def checkClicked():
    loc = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        if loc[0] >= 950 and loc[0] <= 1150:
            if loc[1] >= 500 and loc[1] <= 550:
                return True


def text_objects(txt, font):
    txtsurf = font.render(txt, False, black)
    return txtsurf


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


def home():
    running = True
    pygame.mixer.music.load('Music/Intro.mp3')
    pygame.mixer.music.play(-1, 0.0)
    imgfr = 0
    timer = 0
    while running:
        if imgfr > 4:
            imgfr = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        displayIntroImage(InArr[imgfr])
        pygame.draw.rect(screen, black, (945, 495, 210, 60))
        pygame.draw.rect(screen, grey, (950, 500, 200, 50))
        txt = pygame.font.Font('freesansbold.ttf', 40)
        textsurf = text_objects('Play', txt)
        screen.blit(textsurf, (1010, 505))
        pygame.display.update()
        timer += 1
        if timer >= 200:
            timer = 0
            imgfr += 1
        if checkClicked():
            pygame.mixer.music.stop()
            break
    return 1


def characterScreen():
    running = True
    r = random.randint(0, 7)
    if r == 0:
        pygame.mixer.music.load('Music/Koushu.mp3')
    elif r == 1:
        pygame.mixer.music.load('Music/Misdirection.mp3')
    elif r == 2:
        pygame.mixer.music.load('Music/Kiseki No Sedai.mp3')
    elif r == 3:
        pygame.mixer.music.load('Music/Midorima Theme.mp3')
    elif r == 4:
        pygame.mixer.music.load('Music/Aomine Theme.mp3')
    elif r == 5:
        pygame.mixer.music.load('Music/Kagami Theme.mp3')
    elif r == 6:
        pygame.mixer.music.load('Music/Shield Of Ageis.mp3')
    pygame.mixer.music.play(-1, 0.0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        screen.fill(white)
        displayCharacters()
        pygame.draw.rect(screen, black, (10, 10, 120, 50))
        pygame.draw.rect(screen, grey, (15, 15, 110, 40))
        txt = pygame.font.Font('freesansbold.ttf', 30)
        textsurf = text_objects('Back', txt)
        if checkBack():
            pygame.mixer.music.stop()
            return 0, 0
        if checkSelectedChar():
            pygame.mixer.music.stop()
            return 2, getSelectedChar()
        screen.blit(textsurf, (30, 20))
        pygame.display.update()


def checkBack():
    loc = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        if loc[0] >= 15 and loc[0] <= 125:
            if loc[1] >= 15 and loc[1] <= 55:
                return True


def checkSelectedChar():
    loc = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        if loc[0] >= 175 and loc[0] <= 325:
            if loc[1] >= 50 and loc[1] <= 250:
                return True
        if loc[0] >= 375 and loc[0] <= 525:
            if loc[1] >= 50 and loc[1] <= 250:
                return True
        if loc[0] >= 575 and loc[0] <= 725:
            if loc[1] >= 50 and loc[1] <= 250:
                return True
        if loc[0] >= 775 and loc[0] <= 925:
            if loc[1] >= 50 and loc[1] <= 250:
                return True
        if loc[0] >= 300 and loc[0] <= 450:
            if loc[1] >= 320 and loc[1] <= 520:
                return True
        if loc[0] >= 500 and loc[0] <= 650:
            if loc[1] >= 320 and loc[1] <= 520:
                return True
        if loc[0] >= 700 and loc[0] <= 850:
            if loc[1] >= 320 and loc[1] <= 520:
                return True


def getSelectedChar():
    loc = pygame.mouse.get_pos()
    if loc[0] >= 175 and loc[0] <= 325:
        if loc[1] >= 50 and loc[1] <= 250:
            return 1
    if loc[0] >= 375 and loc[0] <= 525:
        if loc[1] >= 50 and loc[1] <= 250:
            return 2
    if loc[0] >= 575 and loc[0] <= 725:
        if loc[1] >= 50 and loc[1] <= 250:
            return 3
    if loc[0] >= 775 and loc[0] <= 925:
        if loc[1] >= 50 and loc[1] <= 250:
            return 4
    if loc[0] >= 300 and loc[0] <= 450:
        if loc[1] >= 320 and loc[1] <= 520:
            return 5
    if loc[0] >= 500 and loc[0] <= 650:
        if loc[1] >= 320 and loc[1] <= 520:
            return 6
    if loc[0] >= 700 and loc[0] <= 850:
        if loc[1] >= 320 and loc[1] <= 520:
            return 7


def useSpecialAbility1(cc):
    if cc == 1:

    elif cc == 2:

    elif cc == 3:

    elif cc == 4:

    elif cc == 5:

    elif cc == 6:

    elif cc == 7:

def useSpecialAbility2(cc):
    if cc == 1:

    elif cc == 2:

    elif cc == 3:

    elif cc == 4:

    elif cc == 5:

    elif cc == 6:

    elif cc == 7:

def main(charcode):
    r = random.randint(0, 7)
    s1 = None
    if r == 0:
        s1 = pygame.mixer.Sound('Music/Koushu.ogg')
    elif r == 1:
        s1 = pygame.mixer.Sound('Music/Misdirection.ogg')
    elif r == 2:
        s1 = pygame.mixer.Sound('Music/Kiseki No Sedai.ogg')
    elif r == 3:
        s1 = pygame.mixer.Sound('Music/Midorima Theme.ogg')
    elif r == 4:
        s1 = pygame.mixer.Sound('Music/Aomine Theme.ogg')
    elif r == 5:
        s1 = pygame.mixer.Sound('Music/Kagami Theme.ogg')
    elif r == 6:
        s1 = pygame.mixer.Sound('Music/Shield Of Ageis.ogg')
    pygame.mixer.Channel(0).play(s1)
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
            s2 = pygame.mixer.Sound('Music/BOUNCE.ogg')
            pygame.mixer.Channel(1).play(s2)
        if y < 250:
            collision = False
        if lev_y > 550:
            lev_col = True
        if lev_y < 450:
            lev_col = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if powerLevel == 1:
                        useSpecialAbility1(charcode)
                    elif powerLevel < 1 and powerLevel > 0.5:
                        useSpecialAbility2(charcode)
                if event.key == pygame.K_SPACE:
                    lever_lock = True
                elif event.key == pygame.K_a and not lever_lock:
                    x -= 20
                    y += 20
                elif event.key == pygame.K_d and not lever_lock:
                    x += 20
                    y += 20
        screen.fill(white)
        displayHoop(width / 2 - 50, 100)
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
            running = False
            pygame.mixer.Channel(0).stop()
            pygame.mixer.Channel(1).stop()
    return 0


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


def displayIntroImage(img):
    screen.blit(img, (0, 0))


def displayBasketBall(bx, by):
    screen.blit(ball, (bx, by))


if __name__ == '__main__':
    clicked = 0
    cc = 0
    while 1:
        if clicked is None:
            exit()
        elif clicked == 0:
            clicked = home()
        elif clicked == 1:
            clicked, cc = characterScreen()
        elif clicked == 2:
            clicked = main(cc)
