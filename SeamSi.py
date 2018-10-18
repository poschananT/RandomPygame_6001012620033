# Poschanan Thongsri 6001012620033
# My Blog : http://poschanan.blogspot.com/

import pygame
import random
pygame.init()

width = 350
height = 500

win = pygame.display.set_mode((width,height),pygame.RESIZABLE)
pygame.display.set_caption('SeamSi')
# set window beginning such as caption

num = random.sample(range(1, 29), 28)
# set range of data

while True:
    pygame.draw.rect(win, (255, 255, 255), [25, 25, width - 50, height - 150])
    seamsi = pygame.image.load('seamsee-box-lg.PNG')
    win.blit(seamsi, (-50, 325))
    win.blit(seamsi, (180, 325))
    # import pictrues "seam-si"

    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 1:   # when you click
        if 125 + 100 > pos[0] > 125 and 400 + 100 > pos[1] > 400:    # input x, y values for draw a rectangle and change the color
            pygame.draw.rect(win, (250 ,128 ,114), [125, 400, 100, 50])
            text = pygame.font.SysFont('helvetica', 20).render('Seamsi', True, (0,0,0))
            win.blit(text, (125 + (50 / 2.5), 400 + (50 / 4)))

            pygame.mixer.music.load("button_click_01.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(1)
            # input sound into Seam-si

            num = random.sample(range(1, 29), 28)
            # set range again

    else:
        pygame.draw.rect(win, (255,0,0), [125, 400, 100, 50])
        text = pygame.font.SysFont('helvetica', 20).render('Seamsi', True, (255, 255, 255))
        win.blit(text, ((125 + (50 / 2.5)), (400 + (50 / 4))))
        # "else" this is draw button follow input value beginning

    x = 0
    y = 25
    for e in num[0:7]:
        text = pygame.font.SysFont('helvetica', 35).render(str(e), True, (0, 0, 0))
        win.blit(text, (x + 25 + (50 / 2.5), y + (50 / 4)))
        y += 45

    x = 0
    y = 25
    for e in num[7:14]:
        text = pygame.font.SysFont('helvetica', 35).render(str(e), True, (0, 0, 0))
        win.blit(text, (x + 100 + (50 / 2.5), y + (50 / 4)))
        y += 45

    x = 0
    y = 25
    for e in num[14:21]:
        text = pygame.font.SysFont('helvetica', 35).render(str(e), True, (0, 0, 0))
        win.blit(text, (x + 175 + (50 / 2.5), y + (50 / 4)))
        y += 45

    x = 0
    y = 25
    for e in num[21:28]:
        text = pygame.font.SysFont('helvetica', 35).render(str(e), True, (0, 0, 0))
        win.blit(text, (x + 250 + (50 / 2.5), y + (50 / 4)))
        y += 45
    # input number into rectangular in SeamSi


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # close window

        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)


    pygame.display.update()   # update window

