shape = input("would you like turtle to draw a square, or triangle?")
print(shape)
import turtle 
tg = turtle.Screen()
tg.bgcolor("green")
raphael = turtle.Turtle()
raphael.shape('turtle')
raphael.up()
raphael.goto(0,100)
if shape=='square' or 'Square' or 'SQUARE':
    raphael=turtle.Turtle
    raphael.down()
    raphael.color('red')
    raphael.forward(100)
    raphael.left(90)
    raphael.forward(100)
    raphael.left(90)
    raphael.forward(100)
    raphael.left(90)
    raphael.forward(100)
elif shape== 'triangle' or 'Triangle' or 'TRIANGLE':
    raphael=turtle.Turtle
    raphael.down()
    raphael.color('blue')
    raphael.forward(50)
    raphael.left(120)
    raphael.forward(50)
    raphael.left(120)
    raphael.forward(50)
else:
    print('Sorry but you gave the wrong input, try again!')
tg.exitonclick()




