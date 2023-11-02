import turtle
import tkinter as tk
import random

winter_scene = turtle.Screen()
winter_scene.bgcolor("skyblue")

timeout_duration = 20000  

def close_window():
    turtle.bye()
    return
winter_scene.ontimer(close_window, timeout_duration)

snowflake_turtle = turtle.Turtle()
snowflake_turtle.speed(0)  

def draw_snowflake(size):
    for _ in range(6):
        snowflake_turtle.forward(size)
        snowflake_turtle.backward(size)
        snowflake_turtle.left(60)


def draw_giant_snowflake(x, y):
    snowflake_turtle.penup()
    snowflake_turtle.goto(x, y)
    snowflake_turtle.pendown()
    snowflake_turtle.color("white")
    snowflake_turtle.pensize(random.randint(5,15))
    snowflake_size = random.randint(50, 150)
    draw_snowflake(snowflake_size)


def create_random_snowflake():
    x = random.randint(-turtle.window_width() // 2, turtle.window_width() // 2)
    y = random.randint(-turtle.window_height() // 2, turtle.window_height() // 2)
    draw_giant_snowflake(x, y)


def draw_multiple_snowflakes(num_snowflakes):
    for _ in range(num_snowflakes):
        create_random_snowflake()


def main():
    
    root = tk.Tk()
    root.title("Snowflakes")
    draw_button = tk.Button(root, text="Draw Snowflakes", command=lambda: draw_multiple_snowflakes(3))
    draw_button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()






    



