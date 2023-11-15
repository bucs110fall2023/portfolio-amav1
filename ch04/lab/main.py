import pygame
import random
import math
import sys

#Part B
pygame.init()

pygame.font.init()
font = pygame.font.Font(None, 20)
window= pygame.display.set_mode([400,400])
window_size_variable= pygame.display.get_window_size()
width = window_size_variable[0]
length = window_size_variable[1]
x2 = width/2
y2 = length/2
variable1 = 0
variable2 = 0
variable3 = 0
playerblue = "blue"
playerred = "red"
redcount = 0
bluecount = 0


run = True
font = pygame.font.SysFont(None, 20)
win = font.render("Who do YOU think will win?", True, "white")
playerblue1 = font.render("Blue Player won!", True, "white")
playerred1 = font.render("Red Player won!", True, "white")
tie = font.render("It's a tie!", True, "White")
right1 = font.render("Ayy, you're right!", True, "White")
wrong = font.render("Aww, you're wrong!", True, "White")
result = []

hit_box_width = width/2
hitboxes = {
    "blue": pygame.Rect(0, 0, hit_box_width, length),
    "red": pygame.Rect(0, 0, hit_box_width, length)
}
hitboxes["blue"].left = hitboxes["red"].right
main_colors = {
 "blue": (200, 0, 0),
 "red": (0, 0, 200),
}
flag = 0

for color in main_colors:
    # for c, hb in hitboxes.items():
    #     pygame.draw.rect(window, main_colors[c], hb)
    pygame.draw.rect(window, main_colors[color], hitboxes[color])
    window.blit(win, (80,80))
    pygame.display.flip()
    pygame.time.delay(500)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = 1
            if hitboxes["blue"].collidepoint(event.pos):
                result.append("blue")
                variable1 = 1
            elif hitboxes["red"].collidepoint(event.pos):
                result.append("red")
                variable1 = 2

    #Part A
    if flag == 1:
        window.fill('light blue')
        pygame.draw.circle(window, "pink", (200,200), 200)
        pygame.draw.circle(window, "black", (200,200), 200, 2)
        pygame.draw.line(window, "black", (200, 0), (200, length), 2)
        pygame.draw.line(window, "black", (length, 200), (0, width/2), 2)
        pygame.display.flip()
        pygame.time.wait(500)


        for i in range (0,10):
            x1= random.randint(0, 400)
            y1= random.randint(0, 400)

            distance_from_center = math.hypot(x1-x2, y1-y2) 
            is_in_circle = distance_from_center <= width/2 
            
            if is_in_circle:
                pygame.draw.circle(window, playerblue, (x1,y1), 10)
                variable2 += 1
                bluecount += 1
            else:
                pygame.draw.circle(window, "yellow", (x1,y1), 10)
                pygame.display.flip()
                pygame.time.wait(500)

            x1= random.randint(0, 400)
            y1= random.randint(0, 400)

            distance_from_center = math.hypot(x1-x2, y1-y2) 
            is_in_circle = distance_from_center <= width/2 
            if is_in_circle:
                pygame.draw.circle(window, playerred, (x1,y1), 10)
                variable3 += 1
                redcount += 1
            else:
                pygame.draw.circle(window, "orange", (x1,y1), 10)
                pygame.display.flip()
                pygame.time.wait(1000)
       
        #window.blit(f"", (0, 48)) # where <x> and<y> are coordinates on screen
        if bluecount > redcount:
                print ("Red player wins!")
        if redcount > bluecount:
                print ("Blue player wins!")
        elif bluecount == redcount:
                print ("It's a tie!")
        pass

        if variable3>variable2:
            window.blit(playerred1, (250,250))
            pygame.display.flip()
        elif variable2>variable3:
            window.blit(playerblue1, (250,250))
            pygame.display.flip()
        else:
            window.blit(tie, (250, 250))
            pygame.display.flip()
        run = False

    if flag:
        if variable1 == 1 and variable2>variable3:
            window.blit(right1, (250,300))
            pygame.display.flip()
        elif variable1 == 2 and variable3>variable2:
            window.blit(right1, (250,300))
            pygame.display.flip()
        else:
            window.blit(wrong, (250,300))
<<<<<<< HEAD
    pygame.display.flip()
=======
    pygame.display.flip()
>>>>>>> 87b34754d8414abb8b2447cb001326196353dbd0
