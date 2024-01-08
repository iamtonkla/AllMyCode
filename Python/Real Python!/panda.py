from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=500)
my_turtle.shape('classic')
my_turtle.color('blue', 'white')
my_turtle.shapesize(1, 1, 1)
posi = my_turtle.position()
print(posi)
my_turtle.forward(100)
my_turtle.penup()
my_turtle.pendown()

screen.exitonclick()