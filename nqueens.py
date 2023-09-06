import pygame
import sys
from pygame.locals import *
import argparse
from classes import *
from functions import *
import time

parser = argparse.ArgumentParser(description="N queens, select n*n size, and num of processors")
parser.add_argument("n", type=int)
parser.add_argument("numproc", type=int)
args = parser.parse_args()

boxesWidthHeight = 70
QUANTITY = args.n
NUM_PROCESSOR = args.numproc
OFFSET_Y = 150

#it helps to select which board the user sees
selection = 0

if args.n>12:
    boxesWidthHeight = 40


if args.n <= 2 or args.numproc<1:
    print("Enter n values greater than 2, and in numprocessor values greater or equal to 1")
    sys.exit()

start = time.time()
#it returns an array containing the boards that satisfy the condition
a,ellapsed = begin(QUANTITY,NUM_PROCESSOR)

if a == False or len(a) == 0 :
    print("no solution found, try again, ellapsed {}".format(time.time()-start))
    sys.exit()

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE, 32)
pygame.display.set_caption("N queens")
font = pygame.font.SysFont("monospace", 26)

arrBoxes = createBoxes(boxesWidthHeight,a[selection],QUANTITY,offsetX=390,offsetY=OFFSET_Y)

# Fill background
background = pygame.Surface(screen.get_size())
background.fill((50,50,50))
#background = background.convert()

# Display some text
text = font.render("N Queens, Press M or N to change board, q to exit or close the window, ellapsed to generate answers {} sec".format(round(ellapsed,3)),True, (0,0,0), (255, 255, 255))
text2 = font.render("Given a {}x{} grid, they are allowed {} queens".format(args.n,args.n,args.n-1),0,(250, 250, 250))

img = pygame.image.load("img.png").convert_alpha()
img = pygame.transform.scale(img, (boxesWidthHeight, boxesWidthHeight))

# Event loop
on = True
while on:
    text3 = font.render("We have {} solutions, solution # {} selected".format(len(a),selection+1), 0, (250, 250, 250))

    for e in pygame.event.get():
        if e.type == QUIT:
            on = False
            break
        if e.type == KEYDOWN:
            if (e.unicode) == "q":
                on = False
                break
            elif (e.unicode) == "m":
                selection += 1
                if selection >= len(a):
                    selection = 0
                arrBoxes = createBoxes(boxesWidthHeight,a[selection],QUANTITY,offsetX=390,offsetY=OFFSET_Y)
            elif (e.unicode) == "n":
                selection -= 1
                if selection <= 0:
                    selection = 0
                arrBoxes = createBoxes(boxesWidthHeight,a[selection],QUANTITY,offsetX=390,offsetY=OFFSET_Y)

    screen.blit(background,(0,0))
    drawBoxes(arrBoxes,screen,img)
    screen.blit(text, (70,10))

    screen.blit(text2, (700,50))
    screen.blit(text3, (700,100))

    pygame.display.update()
pygame.quit()

print(ellapsed)
