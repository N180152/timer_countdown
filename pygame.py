import pygame
import math
import time
import random

pygame.init()

screen = pygame.display.set_mode((500, 600))

c1 =  (255,255,0)
c2 = (255, 255, 255)
c3 =(0,0,128)
c4 = 	(255,0,0)
BLACK = (0, 0, 0)
YELLOW = (232, 232, 35)
PURPLE = (128,0,0)

running = True

font = pygame.font.SysFont("sans", 35)
inc = font.render("+", True, c2)
dec = font.render("-", True, c2)
start = font.render("START", True, c2)
reset = font.render("RESET", True, c2)

sMinute = "00"
sSecond = "00"
minute = font.render(sMinute, True, c2)
second = font.render(sSecond, True, c2)

y = 0
x = 0
long = True
ok = False
k = time.localtime().tm_sec

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)

while running:
    screen.fill(BLACK)


    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.draw.rect(screen, c3, (100, 25, 50, 50))
    pygame.draw.rect(screen, c3, (175, 25, 50, 50))
    pygame.draw.rect(screen, c3, (300, 25, 150, 50))


    pygame.draw.rect(screen, c3, (100, 125, 50, 50))
    pygame.draw.rect(screen, c3, (175, 125, 50, 50))
    pygame.draw.rect(screen, c3, (300, 125, 150, 50))

    screen.blit(inc, (113, 20))
    screen.blit(inc, (188, 20))
    screen.blit(dec, (118, 116))
    screen.blit(dec, (193, 116))

    screen.blit(start, (309, 21))
    screen.blit(reset, (309, 122))


    screen.blit(minute, (102, 71))
    screen.blit(second, (177, 71))
    pygame.draw.rect(screen, c2, (160, 92, 5, 5))
    pygame.draw.rect(screen, c2, (160, 102, 5, 5))

    if ok == False:
        pygame.draw.circle(screen, c4, (250, 200 + 150), 125, 7)

    pygame.draw.circle(screen, c2, (250, 200 + 150), 5)
    pygame.draw.rect(screen, c1, (50, 525, 400, 30), 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ok == False and 100 <= mouse_x <= 100 + 50 and 25 <= mouse_y <= 25 + 50:
                    if (int(sMinute) < 59):
                        sMinute = "%02d" % (int(sMinute) + 1)
                        minute = font.render(sMinute, True, c2)
                elif ok == False and 175 <= mouse_x <= 175 + 50 and 25 <= mouse_y <= 25 + 50:
                    if (int(sSecond) < 59):
                        sSecond = "%02d" % (int(sSecond) + 1)
                        second = font.render(sSecond, True, c2)
                elif ok == False and 300 <= mouse_x <= 300 + 150 and 25 <= mouse_y <= 25 + 50:
                    ok = True
                elif ok == False and 100 <= mouse_x <= 100 + 50 and 125 <= mouse_y <= 125 + 50:
                    if (int(sMinute) > 0):
                        sMinute = "%02d" % (int(sMinute) - 1)
                        minute = font.render(sMinute, True, c2)
                elif ok == False and 175 <= mouse_x <= 175 + 50 and 125 <= mouse_y <= 125 + 50:
                    if (int(sSecond) > 0):
                        sSecond = "%02d" % (int(sSecond) - 1)
                        second = font.render(sSecond, True, c2)
                elif 300 <= mouse_x <= 300 + 150 and 125 <= mouse_y <= 125 + 50:
                    sMinute = "00"
                    sSecond = "00"
                    minute = font.render(sMinute, True, c2)
                    second = font.render(sSecond, True, c2)
                    ok = False
                    x = 0
                    y = 0

            elif ok == False and event.button == 5:
                if 100 <= mouse_x <= 100 + 50 and 25 + 50 <= mouse_y <= 125:
                    if (int(sMinute) < 59):
                        sMinute = "%02d" % (int(sMinute) + 1)
                        minute = font.render(sMinute, True, c2)
                elif 175 <= mouse_x <= 175 + 50 and 25 + 50 <= mouse_y <= 125:
                    if (int(sSecond) < 59):
                        sSecond = "%02d" % (int(sSecond) + 1)
                        second = font.render(sSecond, True, c2)
            elif ok == False and event.button == 4:
                if 100 <= mouse_x <= 100 + 50 and 25 + 50 <= mouse_y <= 125:
                    if (int(sMinute) > 0):
                        sMinute = "%02d" % (int(sMinute) - 1)
                        minute = font.render(sMinute, True, c2)
                elif 175 <= mouse_x <= 175 + 50 and 25 + 50 <= mouse_y <= 125:
                    if (int(sSecond) > 0):
                        sSecond = "%02d" % (int(sSecond) - 1)
                        second = font.render(sSecond, True, c2)

    if ok:
        if k != time.localtime().tm_sec:
            if int(sSecond) > 0:
                sSecond = "%02d" %(int(sSecond) - 1)
                second = font.render(sSecond, True, c2)
            elif int(sMinute) > 0:
                sSecond = "59"
                sMinute = "%02d" %(int(sMinute) - 1)
                second = font.render(sSecond, True, c2)
                minute = font.render(sMinute, True, c2)
            else:
                ok = False

            k = time.localtime().tm_sec

        if y == 0:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
        pygame.draw.circle(screen, (r, g, b), (250, 200 + 150), 125, 7)

        if y < 60:
            y = y + 1 / 50
        else:
            y = 0
        pygame.draw.line(screen, YELLOW, (250, 200 + 150), (250 + 110 * math.sin(
            math.radians(6 * y)), 200 + 150 - 110 * math.cos(math.radians(6 * y))), 2)

        if long:
            if x < 400:
                x = x + 1 / 5
            else:
                long = False
        else:
            if x > 0:
                x = x - 1 / 5
            else:
                long = True
                x = 0

        if x == 0:
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
        pygame.draw.rect(screen, (red, green, blue), (50, 525, x, 30))


    pygame.display.flip()

pygame.quit()
