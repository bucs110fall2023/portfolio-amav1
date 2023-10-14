import pygame
import random
import math
import sys
pygame.init()
window= pygame.display.set_mode([500,500])


size= pygame.display.get_window_size()


t=0


width = size[0]
x2 = width/2


length = size[1]
y2 = length/2
player1= "red"
player2= "blue"
g=0
h=0


run = True
font = pygame.font.SysFont(None, 48)
text1 = font.render("Player 1 won!", True, "white")
text2 = font.render("Player 2 won!", True, "white")
text3 = font.render("It's a tie!", True, "white")
text4= font.render("Click on who will win!", True, "White")
text5= font.render("You bet right!", True, "White")
text6= font.render("You bet wrong!", True, "White")


result = []


hit_box_width = width / 2


hitboxes = {
    "red": pygame.Rect(0, 0, hit_box_width, length),
    "blue": pygame.Rect(0, 0, hit_box_width, length)
}


hitboxes["red"].left = hitboxes["blue"].right
main_colors = {
 "red": (200, 0, 0),
 "blue": (0, 0, 200),
}


flag = 0


while run:
    for color in main_colors:
                 for c, hb in hitboxes.items(): #reset boxes to main color
                     pygame.draw.rect(window, main_colors[c], hb)
                 pygame.draw.rect(window, main_colors[color], hitboxes[color])
                 window.blit(text4, (60,100))
                 pygame.display.flip()
                 pygame.time.delay(2000)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = 1
            if hitboxes["red"].collidepoint(event.pos):
                result.append("red")
                t = 1
            elif hitboxes["blue"].collidepoint(event.pos):
                result.append("blue")
                t = 2


    if flag == 1:
        window.fill('black')
        pygame.draw.circle(window, "white", (size[0]/2,size[1]/2), size[0]/2)
        pygame.draw.circle(window, "grey", (size[0]/2,size[1]/2), size[0]/2 - 10)
        pygame.draw.line(window, "yellow", [250,0],[250,500])
        pygame.draw.line(window, "yellow", [0,250],[500,250])

        pygame.display.flip()
        pygame.time.wait(500)


        for i in range (0,10):
            x= random.randrange(0, 500)
            y= random.randrange(0, 500)




            distance_from_center = math.hypot(x-x2, y-y2) #the distance formula
            is_in_circle = distance_from_center <= width/2 #screen width
            if is_in_circle:
                pygame.draw.circle(window, player1, (x,y), 10)
                g += 1
            else:
                pygame.draw.circle(window, "purple", (x,y), 10)
            pygame.display.flip()
            pygame.time.wait(1000)




            x= random.randrange(0, 500)
            y= random.randrange(0, 500)




            distance_from_center = math.hypot(x-x2, y-y2) #the distance formula
            is_in_circle = distance_from_center <= width/2 #screen width
            if is_in_circle:
                pygame.draw.circle(window, player2, (x,y), 10)
                h += 1
            else:
                pygame.draw.circle(window, "green", (x,y), 10)
            pygame.display.flip()
            pygame.time.wait(2000)


        if h>g:
            window.blit(text2, (250,250))
            pygame.display.flip()
        elif g>h:
            window.blit(text1, (250,250))

            pygame.display.flip()
        else:
            window.blit(text3, (250, 250))
            pygame.display.flip()
            run = False


    if t==1 and g>h:
        window.blit(text5, (250,300))
        pygame.display.flip()
    elif t==2 and h>g:
        window.blit(text5, (250,300))
        pygame.display.flip()
    else:
        window.blit(text6, (250,300))
        pygame.display.flip()
