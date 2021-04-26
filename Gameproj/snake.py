import pygame
import random
import os

pygame.mixer.init()

# from goto import with_goto

pygame.init()
wid = 900
ht = 600
white=(200,200,200)
red=(255,0,0)
black=(0,0,0)
gameWindow = pygame.display.set_mode((wid,ht))

pygame.display.set_caption("Snake Game")

pygame.display.update()
bgimage = pygame.image.load('grass.jpg')
bgimage = pygame.transform.scale(bgimage,(850,500)).convert_alpha()
Welcome = pygame.image.load('welcome.jpg')
Welcome = pygame.transform.scale(Welcome,(900,600)).convert_alpha()

# Variables

clock = pygame.time.Clock()
fps=30

font = pygame.font.SysFont(None,50)
def prtScore(text,color,x,y):
    text_score= font.render(text, True,color)
    gameWindow.blit(text_score,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:

        pygame.draw.rect(gameWindow,color,[x, y,snake_size, snake_size])

def welcome():
    pygame.mixer.music.load('naagin.mp3')
    pygame.mixer.music.play()
    while True:

        for E in pygame.event.get():
            if E.type == pygame.QUIT:
                quit()
            if E.type == pygame.KEYDOWN:
                if E.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    gameloop()
        gameWindow.fill(white)
        gameWindow.blit(Welcome, (0, 0))
        pygame.display.update()


# pygame.display.update()
def gameloop():
    if(not os.path.exists("hscore.txt")):
        with open("hscore.txt","w") as f:
            f.write("0")
    with open("hscore.txt","r") as f:
        hscore=f.read()
    l = 0
    r = 1
    u = 0
    rad=6
    d = 0
    exit_game = False
    game_over = False
    snake_x = 100
    snake_y = 100
    snake_size = 10
    vel_x = 7
    vel_y = 0
    speed = 7
    food_x = random.randint(45, 700)
    food_y = random.randint(80, 500)
    score = 0

    snk_list = []
    snk_lng = 3


    while not exit_game:

        if game_over:

            with open("hscore.txt","w") as p:
                p.write(str(hscore))

            # gameWindow.fill(white)
            prtScore("GAME OVER!",red,300,150)
            prtScore("Your Score: "+ str(score), red, 300, 200)
            prtScore("High Score: "+str(hscore), red, 300, 250)

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


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
            if snake_x > 860 or snake_y > 530 or snake_x <= 40 or snake_y <= 60:
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                game_over= True
            #     snake_x = 10
            # if :
            #     snake_y = 10
            # if :
            #     snake_x = 900
            # if :
            #     snake_y = 600
            snake_x = snake_x + vel_x
            snake_y = snake_y + vel_y
            if score%5==0 and score != 0:
                rad=10
            else:
                rad = 6
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()


                score+=1
                snk_lng+=2
                if score>int(hscore):
                    hscore=score
                # print("SCORE:",score)

                food_x = random.randint(40, 700)
                food_y = random.randint(60, 500)

            gameWindow.fill(white)
            gameWindow.blit(bgimage,(30,50))
            prtScore("Score: " + str(score), black, 10, 10)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lng:
                del snk_list[0]

            if head in snk_list[:-1]:
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                game_over = True
            plot_snake(gameWindow,black,snk_list,snake_size)
            # pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10])
            pygame.draw.circle(gameWindow,red,[food_x,food_y],rad)
            pygame.draw.rect(gameWindow,black,[20,50,860,10])
            pygame.draw.rect(gameWindow, black, [20,550 , 870, 10])
            pygame.draw.rect(gameWindow, black, [20, 50, 10, 500])
            pygame.draw.rect(gameWindow, black, [880, 50, 10, 500])
        pygame.display.update()
        clock.tick(fps)


welcome()