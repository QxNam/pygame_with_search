# import pygame package
import pygame, sys, random, os
from pygame.locals import *
from search_matrix import Search as qxS
from button import Button as qxB

os.chdir('./pygame_main')

pygame.init()
pygame.mixer.init()
#pygame.mixer.music.load('assets/bg_music.mp3')
#pygame.mixer.music.play(-1)

def cvt100(num):
    return int(num*100)

gray_color = [133,133,133]
black_color = [0, 0, 0]
white_color = [222, 222, 222]
green_color = [127,255,0]
yellow_color=(255, 255, 0)
orange_color=(255, 100, 0)
barry = [(2, 1), (2, 2), (1, 2), (1, 3), (4, 1), (4, 2), (3, 4), (4, 4), (8, 2), (9,3), (6, 8), (7,7), (3,9), (4,8), (4,9), (9, 9), (10, 5), (10, 6)]#[]
sc_size = (1800, 900)
sc_game = (14, 9)

screen = pygame.display.set_mode(sc_size)
logo = pygame.transform.scale(pygame.image.load('assets/logo.png').convert(), (100, 100))
monster = pygame.transform.scale(pygame.image.load('assets/monster.png').convert_alpha(), (100, 100))
land = pygame.transform.scale(pygame.image.load('assets/land.png').convert(), (100, 100))
bg = pygame.transform.scale(pygame.image.load('assets/bg.png').convert(), sc_game)
goal = pygame.transform.scale(pygame.image.load('assets/dragonball.png').convert_alpha(), (100, 100))

spriteL = [pygame.transform.scale(pygame.image.load(f'assets/run{i}.png').convert(), (100, 100)) for i in range(1,4)]
spriteR = [pygame.transform.scale(pygame.image.load(f'assets/run{i}.png').convert(), (100, 100)) for i in range(4,7)]

btn_bfs = pygame.image.load('assets/btn_bfs1.png').convert_alpha()
btn_dfs = pygame.image.load('assets/btn_dfs1.png').convert_alpha()
btn_ids = pygame.image.load('assets/btn_ids1.png').convert_alpha()
btn_greedy = pygame.image.load('assets/btn_greedy1.png').convert_alpha()

pygame.display.set_caption('Qx Running!')
pygame.display.set_icon(logo)

clock = pygame.time.Clock()


def drawGrid():
    blockSize = 100
    for x in range(0, cvt100(sc_game[0]), blockSize):
        for y in range(0, cvt100(sc_game[1]), blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, yellow_color, rect, 1)

def random_pos():
    while True:
        x = random.randint(0, sc_game[0]-1)
        y = random.randint(0, sc_game[1]-1)
        if (x, y) in barry:
            continue
        else:
            return (x, y)


def main():
    o = qxS(sc_game[0], sc_game[1], barry)
    btnB = qxB((1400, 100), btn_bfs, 0.3)
    btnD = qxB((1500, 100), btn_dfs, 0.3)
    btnI = qxB((1600, 100), btn_ids, 0.3)
    btnG = qxB((1700, 100), btn_greedy, 0.3)

    pos_character = (0, 0)
    Alg = 'greedy'
    run = True
    while run:
        i=0; val1=0; val2=0
        pos_goal = random_pos()
        alg = o.runOne(pos_character, pos_goal, Alg)
        way = alg[-1]

        Font=pygame.font.SysFont('timesnewroman',  40)
        name = Font.render(alg[0], False, black_color, yellow_color)
        time_run = Font.render(f"Time: %.5f ms"%(alg[1]), False, green_color, gray_color)
        num_st = Font.render(f"Numbers of steps: {len(way)}", False, green_color, gray_color)
  
        while i<len(way):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            clock.tick(8) # fps
            screen.fill((156,102,31))
            #screen.blit(bg, (0,0))
            drawGrid()
            for j in barry:
                screen.blit(monster, (cvt100(j[0]), cvt100(j[1])))
            for j in way:
                screen.blit(land, (cvt100(j[0]), cvt100(j[1])))
            screen.blit(goal, (cvt100(pos_goal[0]), cvt100(pos_goal[1])))
            if pos_character[0] > pos_goal[0]:
                screen.blit(spriteL[val1%3], (cvt100(way[i][0]), cvt100(way[i][1])))
                val1+=1
            else:
                screen.blit(spriteR[val2%3], (cvt100(way[i][0]), cvt100(way[i][1])))
                val2+=1

            if btnB.draw(screen):
                Alg = 'bfs'
            elif btnD.draw(screen):
                Alg = 'dfs'
            elif btnI.draw(screen):
                Alg = 'ids'
            elif btnG.draw(screen):
                Alg = 'greedy'

            screen.blit(name, (1420, 200))
            screen.blit(time_run, (1420, 300))
            screen.blit(num_st, (1420, 400))
            i+=1
            pygame.display.update()
        pos_character = pos_goal

main()