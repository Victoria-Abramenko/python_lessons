import pygame, sys, random
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.newBlock = False

        self.headup = pygame.image.load('headup.png').convert_alpha()
        self.headdown = pygame.image.load('headdown.png').convert_alpha()
        self.headleft = pygame.image.load('headleft.png').convert_alpha()
        self.headright = pygame.image.load('headright.png').convert_alpha()

        self.bodyvertical = pygame.image.load('bodyvertical.png').convert_alpha()
        self.bodyhorizontal = pygame.image.load('bodyhorizontal.png').convert_alpha()

        self.upleft = pygame.image.load('upleft.png').convert_alpha()
        self.upright = pygame.image.load('upright.png').convert_alpha()
        self.downleft = pygame.image.load('downleft.png').convert_alpha()
        self.downright =  pygame.image.load('downright.png').convert_alpha()

        self.tailup = pygame.image.load('tailup.png').convert_alpha()
        self.taildown = pygame.image.load('taildown.png').convert_alpha()
        self.tailleft = pygame.image.load('tailleft.png').convert_alpha()
        self.tailright = pygame.image.load('tailright.png').convert_alpha()

        self.crunchSound = pygame.mixer.Sound('crunchSound.mp3')

    def drawSnake(self):
        self.updateHeadGraphics()
        self.updateTailGraphics()

        for index, block in enumerate(self.body):
            xPos = int(block.x * cellSize)
            yPos = int(block.y * cellSize)
            blockRect = pygame.Rect(xPos, yPos, cellSize, cellSize)

            if index == 0:
                screen.blit(self.head, blockRect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, blockRect)
            else:
                previousBlock = self.body[index + 1] - block
                nextBlock = self.body[index - 1] - block
                if previousBlock.x == nextBlock.x:
                    screen.blit(self.bodyvertical, blockRect)
                elif previousBlock.y == nextBlock.y:
                    screen.blit(self.bodyhorizontal, blockRect)
                else:
                    if previousBlock.x == - 1 and nextBlock.y == - 1 or previousBlock.y == - 1 and nextBlock.x == - 1:
                        screen.blit(self.upleft, blockRect)
                    elif previousBlock.x == - 1 and nextBlock.y == 1 or previousBlock.y == 1 and nextBlock.x == - 1:
                        screen.blit(self.downleft, blockRect)
                    elif previousBlock.y == 1 and nextBlock.x == 1 or previousBlock.x == 1 and nextBlock.y == 1:
                        screen.blit(self.downright, blockRect)
                    elif previousBlock.x == 1 and nextBlock.y == - 1 or previousBlock.y == - 1 and nextBlock.x == 1:
                        screen.blit(self.upright, blockRect)

            # else:
            #     pygame.draw.rect(screen, (105, 84, 127), blockRect)

    def updateHeadGraphics(self):
        headRelation = self.body[1] - self.body[0]
        if headRelation == Vector2(-1, 0):
            self.head = self.headright
        elif headRelation == Vector2(1, 0):
            self.head = self.headleft
        elif headRelation == Vector2(0, 1):
            self.head = self.headup
        elif headRelation == Vector2(0, -1):
            self.head = self.headdown

    def updateTailGraphics(self):
        tailRelation = self.body[-2] - self.body[-1]
        if tailRelation == Vector2(-1, 0):
            self.tail = self.tailright
        elif tailRelation == Vector2(1, 0):
            self.tail = self.tailleft
        elif tailRelation == Vector2(0, 1):
            self.tail = self.tailup
        elif tailRelation == Vector2(0, -1):
            self.tail = self.taildown

        # for block in self.body:
        #     xPos = int(block.x * cellSize)
        #     yPos = int(block.y * cellSize)
        #     blockRect = pygame.Rect(xPos, yPos, cellSize, cellSize)
        #     pygame.draw.rect(screen, (105, 84, 127), blockRect)

    def moveSnake(self):
        if self.newBlock == True:
            copyBody = self.body[:]
            copyBody.insert(0, copyBody[0] + self.direction)
            self.body = copyBody[:]
            self.newBlock = False
        else:
            copyBody = self.body[:-1]
            copyBody.insert(0, copyBody[0] + self.direction)
            self.body = copyBody[:]

    def addBlock(self):
        self.newBlock = True

    def playCrunchSound(self):
        self.crunchSound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)



class Fruit:
    def __init__(self):
        self.randomize()

    def drawFruit(self):
        xPos = int(self.pos.x * cellSize)
        yPos = int(self.pos.y * cellSize)
        fruitRect = pygame.Rect(xPos, yPos, cellSize, cellSize)
        screen.blit(apple, fruitRect)
        # pygame.draw.rect(screen, (244, 101, 105), fruitRect)

    def randomize(self):
        self.x = random.randint(0, cellNumber - 1)
        self.y = random.randint(0, cellNumber - 1)
        self.pos = Vector2(self.x, self.y)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkFail()

    def drawElements(self):
        self.grassDraw()
        self.fruit.drawFruit()
        self.snake.drawSnake()
        self.drawScore()

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.addBlock()
            self.snake.playCrunchSound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def checkFail(self):
        if not 0 <= self.snake.body[0].x < cellNumber or not 0 <= self.snake.body[0].y < cellNumber:
            self.gameOver()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameOver()

    def grassDraw(self):
        grassColor = (143, 208, 204)
        for row in range(cellNumber):
            if row % 2 == 0:
                for col in range(cellNumber):
                    if col % 2 == 0:
                        grassRect = pygame.Rect(col * cellSize, row * cellSize, cellSize, cellSize)
                        pygame.draw.rect(screen, grassColor, grassRect)
            else:
                for col in range(cellNumber):
                    if col % 2 != 0:
                        grassRect = pygame.Rect(col * cellSize, row * cellSize, cellSize, cellSize)
                        pygame.draw.rect(screen, grassColor, grassRect)

    def gameOver(self):
        self.snake.reset()

    def drawScore(self):
        scoreText = str(len(self.snake.body) - 3)
        scoreSurface = gameFont.render(scoreText, True, (105, 84, 127))
        scoreX = int(cellSize * cellNumber - 60)
        scoreY = int(cellSize * cellNumber - 40)
        scoreRect = scoreSurface.get_rect(center = (scoreX, scoreY))
        appleRect = apple.get_rect(midright=(scoreRect.left, scoreRect.centery))
        bgRect = pygame.Rect(appleRect.left, appleRect.top, appleRect.width + scoreRect.width, appleRect.height)
        pygame.draw.rect(screen, (109, 177, 176), bgRect)
        pygame.draw.rect(screen, (105, 84, 127), bgRect, 2)
        screen.blit(scoreSurface, scoreRect)
        screen.blit(apple, appleRect)

pygame.mixer.pre_init(44100, -16, 2 , 512)
pygame.init()
cellSize = 30
cellNumber = 20
screen = pygame.display.set_mode((cellSize * cellNumber, cellSize * cellNumber))
clock = pygame.time.Clock()
apple = pygame.image.load('mouse.png').convert_alpha()
gameFont = pygame.font.Font('RubikMoonrocks-Regular.ttf', 25)

screenUpdate = pygame.USEREVENT
pygame.time.set_timer(screenUpdate, 150)

mainGame = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screenUpdate:
           mainGame.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if mainGame.snake.direction.y != 1:
                    mainGame.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if mainGame.snake.direction.y != -1:
                    mainGame.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if mainGame.snake.direction.x != 1:
                    mainGame.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if mainGame.snake.direction.x != -1:
                    mainGame.snake.direction = Vector2(1, 0)


    screen.fill((109, 177, 176))
    mainGame.drawElements()
    pygame.display.update()
    clock.tick(60)