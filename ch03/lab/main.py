import turtle 
import random

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
race_1 = random.randrange(0, 300) 
michelangelo.speed(2)
leonardo.speed(2)
michelangelo.forward(race_1) 
leonardo.forward(race_1)
window.delay(10)
michelangelo.ht()
leonardo.ht()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
michelangelo.st()
leonardo.st()

race_2 = random.randrange(1,10)

for race_2 in range(1, 10):
    michelangelo.forward(race_2)
    leonardo.forward(race_2)

window.exitonclick()

## 5. Your PART A code goes here


# PART B - complete part B here

import pygame
pygame.init()
window = pygame.display.set_mode()

for angle in ():
    angle = 360/4

radians = "math.radians"(angle * _)

x = "xpos" + "side_length" * "math.cos"(radians)

y = "xpos" + "side_length" * "math.cos"(radians)

points = [x, y], [x^1, y^1], [x^2, y^2]

pygame.draw.polygon()




