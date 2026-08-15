import turtle
import math

# ---- Setup ----
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("happy birthday")
screen.setup(width=800, height=800)
screen.tracer(0)  # turn off animation for speed, we'll update manually

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.color("#ffb6c1")  # light pink text

message = "I love you "

# ---- Draw the heart made of text ----
# For several scales (nested heart outlines), place the message
# repeatedly around the parametric heart curve. Smaller scales
# fill in the interior, larger ones form the outline.
for scale in range(1, 17):
    for i in range(120):
        angle = i * (math.pi * 2) / 120

        # Parametric heart equation
        x = 16 * (math.sin(angle) ** 3) * scale
        y = (13 * math.cos(angle) - 5 * math.cos(2 * angle)
             - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * scale

        t.goto(x, y)
        # rotate the text slightly to follow the curve
        heading = math.degrees(angle)
        t.setheading(heading)
        t.write(message, font=("Arial", 8, "normal"))

screen.update()

# Add a centered label
label = turtle.Turtle()
label.hideturtle()
label.penup()
label.color("white")
label.goto(0, -20)
label.write("happy birthday", align="center", font=("Arial", 22, "bold"))

screen.update()
screen.exitonclick()