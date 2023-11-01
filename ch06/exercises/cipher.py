import turtle
import tkinter as tk

# Function to draw a snowflake with a given size
def draw_snowflake(size):
    turtle.color("white")
    turtle.width(5)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    for _ in range(6):
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(60)

# Function to draw multiple snowflakes with different sizes and positions
def draw_snowflakes():
    for _ in range(10):  # Draw 10 snowflakes
        x = random.randint(-300, 300)  # Random x-coordinate
        y = random.randint(-300, 300)  # Random y-coordinate
        size = random.randint(50, 150)  # Random size for snowflake
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        draw_snowflake(size)

# Main function
def main():
    window = tk.Tk()
    window.title("Giant Thick Snowflakes")
    canvas = tk.Canvas(window, width=600, height=600, bg="blue")
    canvas.pack()

    turtle.speed(0)  # Set turtle speed to the fastest
    turtle.hideturtle()  # Hide the turtle cursor
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    draw_snowflakes()  # Draw multiple snowflakes

    turtle.done()  # Finish drawing

    window.mainloop()

    return "Snowflakes drawn successfully!"

# Run the main function if the script is executed
if __name__ == "__main__":
    import random  # Import the random module for random positions and sizes
    result = main()  # Call the main function and store the return value in the variable 'result'
    print(result)  # Print the return value
