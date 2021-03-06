import pygame
import random

#inicijalizacija
pygame.init()
displej = pygame.display.set_mode((540, 540))
pygame.display.update()
pygame.display.set_caption('Ovo je originalni snejk koji opci neje kopija s interneta')


def Loop():
    traje = True

    # 0 -gore, 1 - dole
    # 2 - levo, 3 - desno

    trenutni = 0
    prosli = 0

    boja1 = (255, 0 , 0)
    boja2 = (255, 255, 255)
    boja3 = (0,255,0)
    pozadina = (0, 0, 0)
    x1 = 250
    y1 = 250
    x1_change = 0
    y1_change = 0
    vura = pygame.time.Clock()
    lista = []
    duljina = 1
    foodx = round(random.randrange(50, 530))
    foody = round(random.randrange(50, 530))

    #dok igra traje
    while traje:
        for event in pygame.event.get():
    #        print("Pygame.info: " + str(event))
            if event.type == pygame.QUIT:
                traje = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                    trenutni = 2 #ide levo
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                    trenutni = 3 #ide desno
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                    trenutni = 0 #ide gore
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
                    trenutni = 1 #ide dole

        x1 = x1 + x1_change
        y1 = y1 + y1_change

        if len(lista) > duljina:
            del lista[0]

        if x1 < 40:
            x1 = 535
        elif x1 > 535:
            x1 = 40

        if y1 < 40:
            y1 = 535
        elif y1 > 535:
            y1 = 40

        glavica = []
        glavica.append(x1)
        glavica.append(y1)

        lista.append(glavica)

        displej.fill(pozadina)

        pygame.draw.rect(displej, boja2, [foodx, foody, 10, 10])
        for tocka in lista:
            pygame.draw.rect(displej, boja1, [tocka[0], tocka[1], 10, 10])

        if x1 <= foodx + 10 and x1 >= foodx-10 and y1 <= foody+10 and y1 >= foody-10:
            duljina = duljina + 1
            foodx = round(random.randrange(50, 530))
            foody = round(random.randrange(50, 530))

        ignore = False
        if trenutni == 1 and prosli == 0:
            ignore = True
        elif trenutni == 0 and prosli == 1:
            ignore = True
        elif trenutni == 2 and prosli == 3:
            ignore = True
        elif trenutni == 3 and prosli == 2:
            ignore = True

        if duljina > 1 and not ignore:
            for tocka in lista[:-1]:
                if tocka[0] == x1 and tocka[1] == y1:
                    displej.fill(pozadina)
                    mesg = pygame.font.SysFont("comicsansms", 20).render('Gejm over. Press r to replay or q to quit', True, boja3)
                    displej.blit(mesg, [100, 100])
                    pygame.display.update()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                    pygame.quit()
                                    quit()
                                elif event.key == pygame.K_r:
                                    Loop()
                            vura.tick(25)


        file = open("skor.txt", "r")
        high = file.read()
        if duljina-1 > int(high):
            high = str(duljina-1)
            file = open("skor.txt", "w")
            file.write(high)

        mesg = pygame.font.SysFont("comicsansms", 35).render('Skor: ' + str(duljina-1) + '              Haj skor: ' + high, True, boja3)
        displej.blit(mesg, [10, 10])

        pygame.display.update()
        prosli = trenutni
        vura.tick(25)

Loop()
