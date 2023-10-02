import pygame
import random
import math
screen=pygame.display.set_mode([400, 400])
screen_size_variable=pygame.display.get_window_size()
width= screen_size_variable[0]
height=screen_size_variable[1]
print(width)
print(height)
while True:
    for event in pygame.event.get():

        screen.fill(pygame.Color("black"))
        pygame.draw.circle(screen, "white", (200,200), 200)
        pygame.draw.circle(screen, "red", (200,200), 200, 2)
        pygame.draw.line(screen, "red", (200, 0), (200, height), 2)
        pygame.draw.line(screen, "red", (height, 200), (0, width/2), 2)
        pygame.display.flip()
        pygame.time.wait(5000)

    x2=(width/2)
    y2=(height/2)
    for i in range(10):
        x1=random.randint(0, 400)
        y1=random.randint(0, 400)
        pygame.draw.circle(screen, "red", (x1, y1), 10)
        distance_from_center = math.hypot(x1-x2, y1-y2) 
        pygame.display.flip()
        pygame.time.wait(5000)
        is_in_circle = distance_from_center <= width/2 
       




