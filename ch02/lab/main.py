
import turtle 
import random
import math

#Part A
window = turtle.Screen() 
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() 
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

x=int(random.randrange(1,100))
y=int(random.randrange(1,100))



leonardo.forward(x)
michelangelo.forward(y)

for _ in range(10):
    x = random.randrange(1,10)
    y = random.randrange(1,10)
    leonardo.forward(x)
    michelangelo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

window.exitonclick()

## 5. Your PART A code goes here


# PART B - complete part B here

import pygame
pygame.init()
while True:
    for event in pygame.event.get():
        pass

    window=pygame.display.set_mode()

    num_sides=[3,4,6,20,100,360]
    xpos=500
    ypos=50
    side_length=100
    points=[]

    for _ in(num_sides):
        for i in range (_):
            angle=360/_
            radians=math.radians(angle*i)
            x = xpos + side_length * math.cos(radians)
            y = ypos + side_length * math.sin(radians)
            points.append([x,y])
        window.fill("Blue")
        pygame.draw.polygon(window, "green", points)
        pygame.display.flip()
        pygame.time.wait(500)
        points=[]