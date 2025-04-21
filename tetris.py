import pygame, sys
from copy import deepcopy
from random import choice, randrange

pygame.init()
width, height = 10, 20
tile = 30
screenSize = (width * tile, height * tile)
res = (500, 650)
screenBack = pygame.display.set_mode(res)
screen = pygame.Surface(screenSize)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * tile, y * tile, tile, tile) for x in range(width) for y in range(height)]

figurePosition = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                  [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                  [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                  [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                  [(0, 0), (0, -1), (0, 1), (-1, -1)],
                  [(0, 0), (0, -1), (0, 1), (1, -1)],
                  [(0, 0), (0, -1), (0, 1), (-1, 0)]
                  ]

figures = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in figPos] for figPos in figurePosition]
figureRect = pygame.Rect(0, 0, tile - 2, tile - 2)
field = [[0 for i in range(width)] for j in range(height)]

animCount, animSpeed, animLimit = 0, 60, 2000

bg = pygame.image.load('bg.jpg').convert()
bgGame = pygame.image.load('gamebg.jpg').convert()

mainFont = pygame.font.Font('RubikDirt-Regular.ttf', 45)
font = pygame.font.Font('RubikDirt-Regular.ttf', 25)

titleTetris = mainFont.render('Тетрис', True, (51, 153, 255))
titleScore = font.render('Счет:', True, pygame.Color('white'))
titleRecord = font.render('Рекорд:', True, (158, 245, 233))

getColor = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

figure, nextFigure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, nextColor = getColor(), getColor()

score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

def CheckBorders():
    if figure[i].x < 0 or figure[i].x > width - 1:
        return False
    elif figure[i].y > height - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True

def GetRecord():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')

def SetRecord(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))

while True:
    record = GetRecord()
    dx, rotate = 0, False
    screenBack.blit(bg, (0, 0))
    screenBack.blit(screen, (20, 20))
    screen.blit(bgGame, (0, 0))

    for i in range(lines):
        pygame.time.wait(200)

    for userEvent in pygame.event.get():
        if userEvent.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if userEvent.type == pygame.KEYDOWN:
            if userEvent.key == pygame.K_LEFT:
                dx = -1
            elif userEvent.key == pygame.K_RIGHT:
                dx = 1
            elif userEvent.key == pygame.K_DOWN:
                animLimit = 100
            elif userEvent.key == pygame.K_UP:
                rotate = True

    figureOld = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not CheckBorders():
            figure = deepcopy(figureOld)
            break

    animCount += animSpeed
    if animCount > animLimit:
        animCount = 0
        figureOld = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not CheckBorders():
                for i in range(4):
                    field[figureOld[i].y][figureOld[i].x] = color
                figure, color = nextFigure, nextColor
                nextFigure, nextColor = deepcopy(choice(figures)), getColor()
                animLimit = 2000
                break

    center = figure[0]
    figureOld = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not CheckBorders():
                figure = deepcopy(figureOld)
                break

    line, lines = height - 1, 0
    for row in range(height - 1, - 1, - 1):
        count = 0
        for i in range(width):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < width:
            line -= 1
        else:
            animSpeed += 3
            lines += 1
    score += scores[lines]

    [pygame.draw.rect(screen, (40, 40, 40), iRect, 1) for iRect in grid]

    for i in range(4):
        figureRect.x = figure[i].x * tile
        figureRect.y = figure[i].y * tile
        pygame.draw.rect(screen, color, figureRect)

    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col:
                figureRect.x, figureRect.y = x * tile, y * tile
                pygame.draw.rect(screen, col, figureRect)

    for i in range(4):
        figureRect.x = nextFigure[i].x * tile + 250
        figureRect.y = nextFigure[i].y * tile + 200
        pygame.draw.rect(screenBack, nextColor, figureRect)

    screenBack.blit(titleTetris, (320, -5))
    screenBack.blit(titleScore, (340, 100))
    screenBack.blit(font.render(str(score), True, pygame.Color('white')), (340, 130))
    screenBack.blit(titleRecord, (340, 170))
    screenBack.blit(font.render(str(record), True, (158, 245, 233)), (340, 190))

    for a in range(width):
        if field[0][a]:
            SetRecord(record, score)
            field = [[0 for b in range(width)] for c in range(height)]
            animCount, animSpeed, animLimit = 0, 60, 2000
            score = 0
            for iRect in grid:
                pygame.draw.rect(screen, getColor(), iRect)
                screenBack.blit(screen, (20, 20))
                pygame.display.flip()
                clock.tick(200)

    pygame.display.flip()
    CheckBorders()
    clock.tick(60)
