import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rock Paper Scissor')
font = pygame.font.SysFont(None, 30)

image = pygame.image.load('hand-rock-paper-scissors-clipart-md.png')
screen.blit(image,(0,0))

pygame.draw.rect(screen,(255,0,0),(240,0,20,380))
pygame.draw.rect(screen,(255,0,0),(488,0,20,380))
pygame.draw.rect(screen,(255,0,0),(0,380,800,17))

pygame.display.flip()



def findindex(x):
    a = x[0]
    b = x[1]
    if a>=0 and a<=239 and b>=0 and b<=380:
        index = 0
    elif a>=260 and a<=484 and b>=0 and b<=380:
        index = 1
    elif a >= 505 and a <= 800 and b >= 0 and b <= 380:
        index = 2
    else:
        index = 3

    return index

def findwinner(x,y):
    if x ==3:
        pass
    elif x ==y :
        return 0
    elif (x==0 and y==1) or (x==1 and y==2) or (x==2 and y==0):
        return 1
    else:
        return 2

def display_score(score):
    if score ==0:
        score = "Draw"
    elif score == 1:
        score = "Player Wins"
    else:
        score = "Computer Wins"

    screen.fill((0,0,0))
    screen.blit(image, (0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (240, 0, 20, 380))
    pygame.draw.rect(screen, (255, 0, 0), (488, 0, 20, 380))
    pygame.draw.rect(screen, (255, 0, 0), (0, 380, 800, 17))


    score_text = font.render(f'score:{score}',True,(255,255,255))
    screen.blit(score_text,(350,450))
    pygame.display.flip()

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            choice = random.randint(0,2)
            index = findindex(pos)
            score = findwinner(index,choice)
            display_score(score)


