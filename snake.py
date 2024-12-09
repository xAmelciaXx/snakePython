import pygame
import sys
import time
import random
import math

width = 400
height = 400
delay = 0.3


class Player:
    x = width/2
    y = height/2
    speed = 10
    size = 10
    score = 0
    direction = 0 
    coords = [[width/2, height/2]]
    alive = True

    def checkalive(self):
        for index in range(len(self.coords)):
            if index != 0 and self.coords[index] == self.coords[0]:
                self.alive = False
        if int(self.x) > width or int(self.x) < 0 or int(self.y) > height or int(self.y) < 0:
            self.alive = False

    def updateDirection(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and self.direction != 2:    
                self.direction = 0

            if event.key == pygame.K_UP and self.direction != 3:   
                self.direction = 1

            if event.key == pygame.K_LEFT and self.direction != 0:   
                self.direction = 2

            if event.key == pygame.K_DOWN and self.direction != 1: 
                self.direction = 3

    def updatePosition(self):
        if self.direction == 0:   
            self.x += self.speed

        if self.direction == 1:   
            self.y -= self.speed

        if self.direction == 2:
            self.x -= self.speed

        if self.direction == 3: 
            self.y += self.speed
        self.coords.insert(0, [self.x, self.y])


class Food:

    def __init__(self, target: Player):
        self.target = target
        self.x = random.randint(0, math.floor(width/10)-1)*10
        self.y = random.randint(0, math.floor(height/10)-1)*10
        self.size = 10
        print(str(self.x) + '/' + str(self.y))

    def newCoords(self):
        self.x = random.randint(0, math.floor(width/10)-1)*10
        self.y = random.randint(0, math.floor(height/10)-1)*10

    def update(self):
        if self.x == int(self.target.x) and self.y == int(self.target.y):    
            self.newCoords()
            self.target.score += 1
        else:
            print(self.target.coords)
            self.target.coords.pop()
            print(self.target.coords)
            print()


snake = Player()
apple = Food(snake)

pygame.init()
pygame.display.set_caption('Snek!')

game_window = pygame.display.set_mode((width, height))

while True:

    for event in pygame.event.get():   
        if event.type != pygame.QUIT:
            snake.updateDirection()
        else:
            sys.exit('App closed by user.')

    pygame.draw.rect(game_window, (0, 0, 0), pygame.Rect(0, 0, width, height))

    for coordinates in snake.coords:
        pygame.draw.rect(game_window, (0, 0, 255), pygame.Rect(coordinates[0], coordinates[1], snake.size, snake.size))

    pygame.draw.rect(game_window, (255, 0, 0), pygame.Rect(apple.x, apple.y, apple.size, apple.size))

    game_window.blit(pygame.font.SysFont("monospace", 50).render(str(snake.score), True, (255, 255, 255)), (70, 30))

    if snake.alive:
        snake.updatePosition()
        apple.update()
        snake.checkalive()
    else:
        game_window.blit(pygame.font.SysFont("monospace", 50).render('GAME OVER', True, (255, 255, 255)), (height/2, 150))

    pygame.display.flip()

    time.sleep(delay)
