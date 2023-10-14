import pygame
pygame.init()
import random
import math
screen = pygame.display.set_mode([400,400])
width, height = pygame.display.get_window_size()
running = True

while True:
    for event in pygame.event.get():

        screen.fill(pygame.Color("black"))
        pygame.draw.circle(screen, "white", (200,200), 200)
        pygame.draw.circle(screen, "red", (200,200), 200, 2)
        pygame.draw.line(screen, "red", (200, 0), (200, height), 2)
        pygame.draw.line(screen, "red", (height, 200), (0, width/2), 2)
        pygame.display.flip()
        pygame.time.wait(2000)

    x2 = width/2
    y2 = height/2
    pointblue = 0
    pointred = 0
    radius = 1
    for i in range(10):
        x1=random.randint(0, 400)
        y1=random.randint(0, 400)
        distance_center= math.hypot(x1-x2, y1-y2)
        color1 = "blue" 
        #if distance_center <= radius:
        if distance_center <= x2:
            color1 = "navyblue"
        else:
            pointblue += 1
        pygame.draw.circle(screen, color1, (x1, y1), 10)
        pygame.display.flip()
        pygame.time.wait(2000)
        is_in_circle = distance_center >= width/2
        x1 = random.randint(0,400)
        y1 = random.randint(0,400)
        distance_center = math.hypot(x1-x2, y1-y2)
        color2 = "red"
        if distance_center <= x2: 
            color2 = "maroon"
        else:
            pointred += 1
        
        pygame.draw.circle(screen, color2, (x1, y1), 10)
        pygame.display.flip()
        pygame.time.wait(5000)
        is_in_circle = distance_center <= width/2
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font("Arial", 20)
    text = font.render("text", True, "black")
    screen.blit(screen, (50, -300)) 
    if pointblue > pointred:
            print ("Blue player wins!")
    if pointred > pointblue:
            print ("Red player wins!")
    elif pointblue == pointred:
            print ("It's a tie!")

    
    

 
       
