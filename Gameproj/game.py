import pygame
import random

pygame.init()
wid = 900
ht = 600
white=(200,200,200)
red=(255,0,0)
black=(0,0,0)
gameWindow = pygame.display.set_mode((wid,ht))
l=0
r=0
u=0
d=0
pygame.display.set_caption("Snake Game")

pygame.display.update()

# Variables
exit_game = False
game_over = False
snake_x =45
snake_y=55
snake_size=10
vel_x = 10
vel_y = 0
speed = 10
food_x= random.randint(20,wid/2)
food_y = random.randint(20,ht/2)
clock = pygame.time.Clock()
fps=30
score=0
font = pygame.font.SysFont(None,50)
def prtScore(text,color,x,y):
    text_score= font.render(text, True,color)
    gameWindow.blit(text_score,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:

        pygame.draw.rect(gameWindow,color,[x, y,snake_size, snake_size])



snk_list=[]
snk_lng = 1

# pygame.display.update()

while not exit_game:
    if game_over:
        gameWindow.fill(white)
        prtScore("GAME OVER!",red,wid/3,ht)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                exit_game = True
    else:


        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if l==0:
                    if event.key == pygame.K_RIGHT:
                        vel_x = speed
                        vel_y = 0
                        l = 0
                        r = 1
                        u = 0
                        d = 0





                if r==0:
                    if event.key == pygame.K_LEFT:
                        vel_x = -speed
                        vel_y = 0
                        l = 1
                        r = 0
                        u = 0
                        d = 0


                if d==0:
                    if event.key == pygame.K_UP:
                        vel_y = -speed
                        vel_x = 0
                        l = 0
                        r = 0
                        u = 1
                        d = 0

                if u==0:
                    if event.key == pygame.K_DOWN:
                        vel_y = speed
                        vel_x = 0
                        l = 0
                        r = 0
                        u = 0
                        d = 1
        if snake_x > 890:
            snake_x = 10
        if snake_y > 590:
            snake_y = 10
        if snake_x <= 0:
            snake_x = 900
        if snake_y <= 0:
            snake_y = 600
        snake_x = snake_x + vel_x
        snake_y = snake_y + vel_y
        if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
            score+=1
            snk_lng+=2
            # print("SCORE:",score)

            food_x = random.randint(20, wid / 2)
            food_y = random.randint(20, ht / 2)

        gameWindow.fill(white)
        prtScore("Score: " + str(score), black, 10, 10)
        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list)>snk_lng:
            del snk_list[0]


        plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10])
    pygame.display.update()
    clock.tick(fps)


import pygame
import random

pygame.init()
wid = 900
ht = 600
white=(200,200,200)
red=(255,0,0)
black=(0,0,0)
gameWindow = pygame.display.set_mode((wid,ht))
l=0
r=0
u=0
d=0
pygame.display.set_caption("Snake Game")

pygame.display.update()

# Variables
exit_game = False
game_over = False
snake_x =45
snake_y=55
snake_size=10
vel_x = 10
vel_y = 0
speed = 10
food_x= random.randint(20,wid/2)
food_y = random.randint(20,ht/2)
clock = pygame.time.Clock()
fps=30
score=0
font = pygame.font.SysFont(None,50)
def prtScore(text,color,x,y):
    text_score= font.render(text, True,color)
    gameWindow.blit(text_score,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:

        pygame.draw.rect(gameWindow,color,[x, y,snake_size, snake_size])



snk_list=[]
snk_lng = 1

# pygame.display.update()

while not exit_game:
    if game_over:
        gameWindow.fill(white)
        prtScore("GAME OVER!",red,wid/3,ht)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                exit_game = True
    else:


        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if l==0:
                    if event.key == pygame.K_RIGHT:
                        vel_x = speed
                        vel_y = 0
                        l = 0
                        r = 1
                        u = 0
                        d = 0





                if r==0:
                    if event.key == pygame.K_LEFT:
                        vel_x = -speed
                        vel_y = 0
                        l = 1
                        r = 0
                        u = 0
                        d = 0


                if d==0:
                    if event.key == pygame.K_UP:
                        vel_y = -speed
                        vel_x = 0
                        l = 0
                        r = 0
                        u = 1
                        d = 0

                if u==0:
                    if event.key == pygame.K_DOWN:
                        vel_y = speed
                        vel_x = 0
                        l = 0
                        r = 0
                        u = 0
                        d = 1
        if snake_x > 890:
            game_over = True
            # snake_x = 10

        if snake_y > 590:
            game_over = True
            # snake_y = 10
        if snake_x <= 0:
            game_over = True
            # snake_x = 900
        if snake_y <= 0:
            game_over = True
            # snake_y = 600
        snake_x = snake_x + vel_x
        snake_y = snake_y + vel_y
        if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
            score+=1
            snk_lng+=2
            # print("SCORE:",score)

            food_x = random.randint(20, wid / 2)
            food_y = random.randint(20, ht / 2)

        gameWindow.fill(white)
        prtScore("Score: " + str(score), black, 10, 10)
        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list)>snk_lng:
            del snk_list[0]


        plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10])
    pygame.display.update()
    clock.tick(fps)


